import React from 'react';

export default class Task extends React.Component {

    constructor() {
        super();

    }

    render() {
        return (
            <li className='task' key={this.props.task.id}>
                <div className='task-title'>
                    {this.props.task.name}
                </div>
            </li>
        );
    }
}