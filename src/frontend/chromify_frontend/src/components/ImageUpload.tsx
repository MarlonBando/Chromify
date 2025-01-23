import { useState } from 'react';
import { Grid, Center } from '@mantine/core';
import { IconArrowNarrowRight } from '@tabler/icons-react';
import { callApi } from '../api';
import { isValid } from 'js-base64';

function ImageComparison() {
    const [colororized_image, setColorizedImage] = useState('/src/assets/000000000009 2.jpg'); // Default image path
    const [image, setImage] = useState('/src/assets/000000000009.jpg'); // Default image path
    const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
        const files = event.target.files;
        if (!files) return;
        const file = files[0]; // Get the selected file
        if (file) {
            const imageURL = URL.createObjectURL(file); // Create a temporary URL
            setImage(imageURL); // Update the displayed image
            // Extract the binary and send it
            const formData = new FormData(); // Create FormData object
            formData.append('data', file); // Append the file to FormData
            callApi(formData).then((response) => {
                console.log("yes");
                setColorizedImage(() => {
                    if(isValid(response.colorized_image)){
                        console.log("Valid base64 string");
                        const decodedImage = `data:image/jpeg;base64,${response.colorized_image}`;
                        console.log(decodedImage);
                        return decodedImage;
                    }
                    return '/src/assets/000000000009 2.jpg';
                });
            }).catch((error) => {
                console.error('API call failed:', error);
            });
        }
    };
    return (

        <Grid>
            <Grid.Col span={5}>
                    <div style={{ textAlign: 'center', marginTop: '20px' }}>
                        {/* Display the image */}
                        <img
                            src={image}
                            alt="Uploaded Preview"
                            style={{
                                maxWidth: '400px',
                                maxHeight: '400px',
                                borderRadius: '10px',
                                objectFit: 'cover',
                            }}
                        />
                        <br />
                        {/* Upload button */}
                        <label
                            style={{
                                display: 'inline-block',
                                marginTop: '20px',
                                padding: '10px 20px',
                                backgroundColor: '#007BFF',
                                color: 'white',
                                borderRadius: '5px',
                                cursor: 'pointer',
                            }}
                        >
                            Upload Image
                            <input
                                type="file"
                                accept="image/*"
                                onChange={handleImageUpload}
                                style={{ display: 'none' }} // Hide the default file input
                            />
                        </label>
                    </div>
            </Grid.Col>
            <Grid.Col span={2}>
                <Center style={{ height: '100%' }}>
                    <IconArrowNarrowRight size={48} />
                </Center>
            </Grid.Col>
            <Grid.Col span={5}>
                <div style={{ textAlign: 'center', marginTop: '20px' }}>
                    {/* Display the image */}
                    <img
                        src={colororized_image.startsWith('data:') ? colororized_image : `${colororized_image}`}
                        alt="Colorized Preview"
                        style={{
                            maxWidth: '400px',
                            maxHeight: '400px',
                            borderRadius: '10px',
                            objectFit: 'cover',
                        }}
                    />
                    <br />
                </div>
            </Grid.Col>
        </Grid>
    );
}

export { ImageComparison };
