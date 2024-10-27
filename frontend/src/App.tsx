import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import RouteEntries from './routes/route-entries'

function App() {
  const [count, setCount] = useState(0)

  return (
    <RouteEntries/>
  )
}

export default App
