
import "@mantine/core/styles.css";
// import "@mantine/dates/styles.css";
import './App.css'
import { DoubleHeader } from  './components/DoubleHeader'
import { ImageComparison } from './components/ImageUpload'
import { MantineProvider } from "@mantine/core";

function App() {
  return (
    <MantineProvider defaultColorScheme="light">
    <div style={{ width: '100%', height: '100vh', display: 'flex', flexDirection: 'column', margin: 0, padding: 0 }}>
      <DoubleHeader />
      <ImageComparison />
    </div>
    </MantineProvider>
  )
}

export default App
