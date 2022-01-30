import React from 'react';


const UserItem = ({user}) => {
    return (
        <tr>
        <td>
            {user.username}
        </td>
        <td>
            {user.first_name}
        </td>
        <td>
            {user.last_name}
        </td>
    </tr>
    )
}


const UserList = ({users}) => {
    return (
    <div>
        <table>
            <th>
                Username
            </th>
            <th>
                First Name
            </th>
            <th>
                Last Name
            </th>
            <tbody>
            {users.map((user) => <UserItem user={user} />)}
            </tbody>
        </table>
    </div>


    )

}

export default UserList