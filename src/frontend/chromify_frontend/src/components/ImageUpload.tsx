import { useState } from 'react';
import { Image, FileInput, Grid, Center } from '@mantine/core';
import { IconArrowNarrowRight } from '@tabler/icons-react';
import { callApi } from '../api';
import { Base64, decode } from 'js-base64';


const [colororized_image, setImage] = useState('/src/assets/000000000009  2.jpg'); // Default image path
function GrayImage() {
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
            console.log(formData);
            callApi(formData).then((response) => {
                console.log('API response:', response);

            }).catch((error) => {
                console.error('API call failed:', error);
            });
        }
    };

    return (
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
    );
}


function ColorImage() {
    return (
        <div style={{ textAlign: 'center', marginTop: '20px' }}>
            {/* Display the image */}
            <img
                src={colororized_image}
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
            {/* <label
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
            </label> */}
        </div>
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
            <Grid.Col span={5}>
                <ColorImage />
            </Grid.Col>
        </Grid>
    );
}

export { GrayImage, ColorImage, ImageComparison };
