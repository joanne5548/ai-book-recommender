import { BrowserRouter, Routes, Route } from "react-router-dom"
import 'bootstrap/dist/css/bootstrap.min.css'
import {Container, Row, Col, Button, Alert, Breadcrumb, Card, Form} from 'react-bootstrap'
import Test from './Test'
import FrontPage from './FrontPage'

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<FrontPage />} />
        <Route path='/Test' element={<Test />} />
      </Routes>
    </>
  )
}

export default App
