import { useState } from 'react';
import {Container, Row, Col, Button, Alert, Breadcrumb, Card, Form} from 'react-bootstrap'
import { Typeahead } from 'react-bootstrap-typeahead';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'react-bootstrap-typeahead/css/Typeahead.css';
import 'react-bootstrap-typeahead/css/Typeahead.bs5.css';
import Titles from '../../public/title.json'

function SearchBar() {
    const [selected, setSelected] = useState([]);
    const options = ['Harry Potter 1', 'Hunger Game 1', 'The Way of Kings', 'Animal Farm'];
    const [text, setText] = useState([]);
    
    const book_list = // Start Here

    return (
        <Form>
            <Form.Group>
                <Form.Label>Select your favorite books</Form.Label>
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
    );
};

export default SearchBar;