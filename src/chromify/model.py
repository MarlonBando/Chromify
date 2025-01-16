import timm
import torch
import torch.nn as nn
import torch.nn.functional as F

class UNetEfficientNetV2(nn.Module):
    def __init__(self, encoder_name='tf_efficientnetv2_s', pretrained=True):
        super(UNetEfficientNetV2, self).__init__()
        
        # Encoder from timm
        self.encoder = timm.create_model(encoder_name, pretrained=pretrained, features_only=True)
        # print(self.encoder.feature_info.channels())
        encoder_channels = self.encoder.feature_info.channels()
        
        # Decoder: Upsample and merge skip connections
        self.decoder = nn.ModuleList([
            nn.ConvTranspose2d(encoder_channels[-i], encoder_channels[-i - 1], kernel_size=2, stride=2)
            for i in range(1, len(encoder_channels))
        ])
        
        # Intermediate convolutions for processing skip connections
        self.skip_convs = nn.ModuleList([
            nn.Conv2d(encoder_channels[i], encoder_channels[i], kernel_size=3, padding=1)
            for i in range(len(encoder_channels) - 1)
        ])
        
        # Final convolution layer for AB prediction
        self.final_conv = nn.Conv2d(encoder_channels[0], 2, kernel_size=1)

    def forward(self, x):
        # Pass input through the encoder and collect feature maps
        encoder_features = self.encoder(x)
        x = encoder_features[-1]  # Start from the deepest feature

        # Decoder with skip connections
        for i, decoder_layer in enumerate(self.decoder):
            x = decoder_layer(x)  # Upsample
            skip_feature = encoder_features[-i - 2]  # Get corresponding skip connection
            x = torch.cat([x, skip_feature], dim=1)  # Concatenate skip connection
            x = self.skip_convs[i](x)  # Process concatenated features

        # Final AB prediction
        x = self.final_conv(x)
        return x
