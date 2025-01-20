import { Image } from '@mantine/core';
import { FileInput } from '@mantine/core';
import { IconArrowNarrowRight } from '@tabler/icons-react';
import { Grid, Center} from '@mantine/core';

function GrayImage() {
    return (
        <FileInput
            id="gray-image"
            variant="unstyled"
            size="xl"
            radius="xl"
            label="Gray Image"
            withAsterisk
            description="Gray Image to color"
            placeholder={
                <Image
                    radius="md"
                    src={null}
                    h={400}
                    fallbackSrc="/src/assets/000000000009.jpg"
                />
            }
        />
    );
}

function ColorImage() {
    return (
        <Image
            radius="md"
            src={null}
            h={400}
            fallbackSrc="/src/assets/000000000009 2.jpg"
        />
    );
}

function ImageComparison() {
    return (
        <Grid>
            <Grid.Col span={5}>
                <GrayImage />
            </Grid.Col>
            <Grid.Col span={2}>
                <Center style={{ height: '100%' }}>
                    <IconArrowNarrowRight size={48} />
                </Center>
            </Grid.Col>
            <Grid.Col span={5} style={{ paddingTop: '70px' }}>
                <ColorImage />
            </Grid.Col>
        </Grid>
    );
}

export { GrayImage, ColorImage, ImageComparison };
