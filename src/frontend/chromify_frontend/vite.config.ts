import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',  // This makes Vite listen on all network interfaces
    port: 5137,  // Ensure the port is correctly set
    strictPort: true,  // Optionally, you can force Vite to always use this port
  },
})
