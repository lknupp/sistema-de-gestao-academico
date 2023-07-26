import React from 'react'
import ReactDOM from 'react-dom/client'
import { App, Home } from './App.tsx'
import ErrorPage from './error-page.tsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import './index.css'
import { Student, StudentCreate, Students } from './components/student.tsx'
import { Professor, ProfessorCreate, Professors } from './components/professor.tsx'
import { Course, CourseCreate, Courses } from './components/course.tsx'
import { Discipline, DisciplineCreate, Disciplines } from './components/discipline.tsx'
import { Campuss, Campus, CampusCreate } from './components/campus.tsx'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "aluno",
        element: <Students />,
      },
      {
        path: "aluno/create",
        element: <StudentCreate />,
      },
      {
        path: "aluno/:id",
        element: <Student />,
      },
      {
        path: "professor",
        element: <Professors />,
      },
      {
        path: "professor/:id",
        element: <Professor />,
      },
      {
        path: "professor/create",
        element: <ProfessorCreate />,
      },
      {
        path: "curso",
        element: <Courses />,
      },
      {
        path: "curso/:id",
        element: <Course />,
      },
      {
        path: "curso/create",
        element: <CourseCreate />,
      },
      {
        path: "disciplina",
        element: <Disciplines />,
      },
      {
        path: "disciplina/:id",
        element: <Discipline />,
      },
      {
        path: "disciplina/create",
        element: <DisciplineCreate />,
      },
      {
        path: "campus",
        element: <Campuss />,
      },
      {
        path: "campus/:id",
        element: <Campus />,
      },
      {
        path: "campus/create",
        element: <CampusCreate />,
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
