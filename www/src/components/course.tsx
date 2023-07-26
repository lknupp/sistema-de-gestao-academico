import { Link } from "react-router-dom";
import { Input } from "../App";
import { useState } from "react";

export function Courses() {
  const courses = [
    {
      id: 1,
      nome: 'Ciência da Computação',
    },
    {
      id: 2,
      nome: 'Engenharia de Software'
    }
  ];

  if (courses.length === 0) return (
    <>
      <h1 className="text-3xl">cursos</h1>
      <p className="mt-5">Nenhum curso encontrado.</p>
    </>
  )

  return (
    <>
      <div className="flex items-center justify-between">
        <h1 className="text-3xl">cursos</h1>
        <Link to="/curso/create" className="p-2 mt-2 text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">+ adicionar</Link>
      </div>

      <div className="flex flex-col">
        <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
            <div className="overflow-hidden">
              <table className="min-w-full text-left">
                <thead className="font-medium border-b dark:border-stone-200">
                  <tr>
                    <th scope="col" className="px-6 py-4">nome</th>
                    <th scope="col" className="px-6 py-4">#</th>
                  </tr>
                </thead>
                <tbody>
                  {courses.map((course) => (
                    <tr key={course.id} className="border-b dark:border-stone-200">
                      <td className="px-6 py-4 whitespace-nowrap">{course.nome}</td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <Link to={`/curso/${course.id}`} className="underline">detalhes</Link>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export function Course() {
  const course: any = {
    id: 1,
    nome: 'Ciência da Computação'
  };

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">curso</h1>
        <Link to="/curso" className="p-2 mt-2 text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <div className="flex justify-around gap-10">
        <ul className="flex-grow">
          {Object.keys(course).map((key) => (
            <li key={key} className="w-full py-4 border-b-2 border-opacity-50 border-stone-200">
              <strong>{key}:</strong> {course[key]}
            </li>
          ))}
        </ul>

        <div className="flex-1">
          <img src="https://placekitten.com/200/200" alt="Foto do curso" />
        </div>
      </div>

    </>
  )
}

export function CourseCreate() {
  const [course, setCourse] = useState({
    nome: ''
  });

  function handleChange(event: any) {
    const { name, value } = event.target;
    setCourse({ ...course, [name]: value });
  }

  function handleSubmit(event: any) {
    event.preventDefault();
    console.log(course);
  }

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">adicionar curso</h1>
        <Link to="/curso" className="p-2 mt-2 text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <form className="grid grid-cols-2 gap-4 mt-5" onSubmit={handleSubmit}>
        <Input label="nome" name="nome" value={course.nome} onChange={handleChange} />
      </form>

      <button className="p-2 mt-5 text-white w-min bg-zinc-900 hover:bg-zinc-700">enviar</button>
    </>
  )
}
