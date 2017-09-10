import React from 'react';

export default class Task extends React.Component {

    constructor() {
        super();
        this.state = {showImage: true};
        this.completeTask = this.completeTask.bind(this);
        this.removeTask = this.removeTask.bind(this);
    }


    completeTask(e) {
        e.preventDefault();
        var data = {'task': this.props.task.id};
        $.ajax({
            type: 'POST',
            url: '/api/v1/task/completed/',
            data: data,
            datatype: 'json',
            success: function(data) {
                console.log('success');
                this.setState({showImage: false});
            }.bind(this),
            error: function(error) {
                console.log('error');
            }
        });
    }

    removeTask(e) {
        e.preventDefault();
        var data = {'task': this.props.task.id};
        $.ajax({
            type: 'POST',
            url: '/api/v1/task/delete/',
            data: data,
            datatype: 'json',
            success: function(data) {
                console.log('success');
                this.setState({showImage: false});
            }.bind(this),
            error: function(error) {
                console.log('error');
            }
        });
    }

    render() {
        var show = this.state.showImage;
        return show && (
            <li className='task' key={this.props.task.id}>
                <div className='task-title'>
                    {this.props.task.name}
                </div>
                <span className="glyphicon glyphicon-ok task-glyph" aria-hidden="true" onClick={this.completeTask}/>
                <span className="glyphicon glyphicon-remove task-glyph" aria-hidden="true" onClick={this.removeTask} />
            </li>
        );
    }
}