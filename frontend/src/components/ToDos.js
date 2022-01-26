import React from 'react';


const ToDoItem = ({todo}) => {
    return (
        <tr>
        <td>
            {todo.related_project}
        </td>
        <td>
            {todo.text}
        </td>
        <td>
            {todo.owner}
        </td>
    </tr>
    )
}


const ToDoList = ({todos}) => {
    return (
        <table>
        <th>
            Project
        </th>
        <th>
            Repo link
        </th>
        <th>
            Related users
        </th>
        <tbody>
        {todos.map((todo) => <ToDoItem todo={todo} />)}
        </tbody>
    </table>

    )
}

export default ToDoList