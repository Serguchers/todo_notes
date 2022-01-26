import React from 'react';
import { useParams, Link } from 'react-router-dom';


const ProjectItem = ({project}) => {
    return (
        <li><Link to={`projects/${project.id}`}>{project.project_name}</Link></li>
    )
}

const ProjectDetail = ({projects}) => {
    let {id} = useParams()
    let filtered_project = projects.filter((project) => project.id == id)[0]
    return (
        
          <p>{filtered_project.project_name} </p>
        
    )
}

const ProjectList = ({projects}) => {
    return (
        <ul>
        {projects.map((project) => <ProjectItem project={project} />)}
        </ul>
    )
}

export {ProjectList, ProjectDetail}