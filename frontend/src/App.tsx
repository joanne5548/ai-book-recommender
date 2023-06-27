import { BrowserRouter, Routes, Route } from "react-router-dom"
import 'bootstrap/dist/css/bootstrap.min.css'
import {Container, Row, Col, Button, Alert, Breadcrumb, Card, Form} from 'react-bootstrap'
import Test from './Test'
import FrontPage from './FrontPage'

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Test />} />
        <Route path='/FrontPage' element={<FrontPage />} />
      </Routes>
    </>
  )
}

export default App
