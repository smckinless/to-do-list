import React from 'react';
import ReactDOM from 'react-dom'
import ToDoList from './toDoList'

export default class App extends React.Component {

    render() {
        return (
            <div className='main'>
                <p className='title'>To-do List App</p>
                <ToDoList />
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('container'));