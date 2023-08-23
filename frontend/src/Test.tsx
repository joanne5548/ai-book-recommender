import 'bootstrap/dist/css/bootstrap.min.css'
import {Container, Row, Col, Button, Alert, Breadcrumb, Card, Form} from 'react-bootstrap'
import './App.css'

function Test() {
    return (
    <div className="App">
      <img src={header} alt="header" class="img-fluid" />
      <Breadcrumb>
        <Breadcrumb.Item>Joanne</Breadcrumb.Item>
        <Breadcrumb.Item>Angela</Breadcrumb.Item>
        <Breadcrumb.Item active>Sam</Breadcrumb.Item>
      </Breadcrumb>

      <Card className="mb-2" key='Dark'>
        <Card.Img src='data:image/jpeg;base64,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'/>
        <Card.Body>
          <Card.Title>
            Card Heehee
          </Card.Title>
          <Card.Text>
            hai hai
          </Card.Text>
          <Button variant="primary">Read more :D</Button>
        </Card.Body>
      </Card>

      <Alert variant="danger">ALERTTTTT</Alert>

      <Container>
        <Form className="mb-2">
          <Row>
            <Col md>
              <Form.Group controlID="formEmail">
                <Form.Label>GIMME YOUR EMAIL</Form.Label>
                <Form.Control type='email' placeholder='example@gmail.com'></Form.Control>
              </Form.Group>
            </Col>
            <Col md>
              <Form.Group controlID='formPassword'>
                <Form.Label>PASSWORD</Form.Label>
                <Form.Control type="password" placeholder="Password"></Form.Control>
                <Form.Text>We will never sell your info :)))</Form.Text>
              </Form.Group>
            </Col>
          </Row>
        </Form>
        <Button>Submit!</Button>
      </Container>
      
    </div>
    )
}

export default Test;