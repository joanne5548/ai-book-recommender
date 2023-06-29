import { useState } from 'react';
import {Container, Row, Col, Button, Alert, Breadcrumb, Card, Form} from 'react-bootstrap'
import { Typeahead } from 'react-bootstrap-typeahead';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'react-bootstrap-typeahead/css/Typeahead.css';
import 'react-bootstrap-typeahead/css/Typeahead.bs5.css';
import Books from '../../public/books.json'
import header from '../assets/Header.png'

function SearchBar() {
    const [selected, setSelected] = useState([]);
    const options = ['Harry Potter 1', 'Hunger Game 1', 'The Way of Kings', 'Animal Farm'];
    const [text, setText] = useState([]);

    return (
        <div>
            <h1 className="mt-4 position-absolute top-0 start-50 translate-middle-x">
                Welcome to AI Book Recommender!
            </h1>

            <Container>
                <Row>
                    <p class="text-center fs-5">Select your favorite books</p>
                    <Col class="col-md-5 offset-md-3">
                        <Form>
                            <Form.Group>
                                <Typeahead
                                    id='basic-typeahead'
                                    labelKey='name'
                                    multiple
                                    onChange={setSelected}
                                    options={options}
                                    placeholder="Click here to search"
                                    selected={selected}
                                    />
                            </Form.Group>
                        </Form>
                    </Col>
                    
                    <Col class="col-md-1">
                        <Button>
                            Done
                        </Button>
                    </Col>
                </Row>
            </Container>
        
        </div>
        
    );
};

export default SearchBar;