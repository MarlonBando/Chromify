
import "@mantine/core/styles.css";
// import "@mantine/dates/styles.css";
import './App.css'
import { DoubleHeader } from  './components/DoubleHeader'
import { MantineProvider } from "@mantine/core";

function App() {

  return (
    <MantineProvider defaultColorScheme="light">
      <DoubleHeader />
    </MantineProvider>
  )
}

export default App
