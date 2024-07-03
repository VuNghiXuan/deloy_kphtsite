// ... (get video stream)

const canvasElement = document.createElement('canvas');
canvasElement.width = videoElement.videoWidth;
canvasElement.height = videoElement.videoHeight;
const context = canvasElement.getContext('2d');

// Use jsQR to detect barcodes
setInterval(() => {
    context.drawImage(videoElement, 0, 0);
    const imageData = context.getImageData(0, 0, canvasElement.width, canvasElement.height);
    const code = jsQR(imageData.data, imageData.width, imageData.height);
    if (code) {
        console.log("Mã vạch:", code.data); // Log detected barcode data
        // Optionally send data to server using AJAX or WebSocket
    }
}, 100); // Adjust interval as needed
