import React from 'react';
import Task from './task';
import NewTask from './new-task';

export default class ToDoList extends React.Component {

    constructor() {
        super();
        this.state = {data: []};
    }

    callServer() {
        /* Get all tasks from API */
        $.ajax({
            url: '/api/v1/task/get/completed/',
            datatype: 'json',
            success: function(data) {
                this.setState({data:JSON.parse(data)});
            }.bind(this),
            error: function(data) {
                console.log(data);
            }
        });
    }

    componentDidMount() {
        this.callServer();
    }

    render() {
        var tasks = [];
        if (this.state.data) {
            tasks = this.state.data.map(function(task) {
                return (<Task key={task.id} task={task} />);
            });
        }
        var newTask = <NewTask />;
        return (
            <ul className='toDoList'>
                {newTask}
                {/*<li className='task'>
                <div className='task-title'>
                    Current Tasks
                </div>
                </li>*/}
                {tasks}
            </ul>
        );
    }
}