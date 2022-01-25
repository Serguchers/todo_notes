import React from 'react';


const ProjectItem = ({project}) => {
    return (
        <li>{project.project_name}</li>
    )
}


const ProjectList = ({projects}) => {
    return (
        <ul>
        {projects.map((project) => <ProjectItem project={project} />)}
        </ul>
    )
}

export default ProjectList