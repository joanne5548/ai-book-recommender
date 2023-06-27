import {useState} from 'react';
import {Container, Row, Col, Button, Alert, Breadcrumb, Card, Form} from 'react-bootstrap'
import { Typeahead } from 'react-bootstrap-typeahead';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'react-bootstrap-typeahead/css/Typeahead.css';
import 'react-bootstrap-typeahead/css/Typeahead.bs5.css';

function FrontPage() {
    const [multiSelections, setMultiSelections] = useState([]);
    const options = ['Harry Potter 1', 'Hunger Game 1', '???']
    return (
        <Form>
            <Form.Group>
                <Form.Label>Select your favorite books</Form.Label>
                <Typeahead
                    id='basic-typeahead-multiple'
                    labelKey='name'
                    multiple
                    onChange={setMultiSelections}
                    options={options}
                    placeholder="Choose books!"
                    selected={MultiSelections}
                    />
            </Form.Group>
        </Form>
    );
}

export default FrontPage;