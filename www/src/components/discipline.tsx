import { Link } from "react-router-dom";
import { Input, Search } from "../App";
import { useState } from "react";
import { LiaFileAltSolid, LiaTrashAltSolid } from "react-icons/lia";

export function Disciplines() {
  const disciplines = [
    {
      id: 1,
      nome: 'Algortimos e Programação',
      descricao: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, vitae aliquam nis',
      id_curso: 'Ciência da Computação',
    },
    {
      id: 2,
      nome: 'Estrutura de Dados',
      descricao: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, vitae aliquam nis',
      id_curso: 'Ciência da Computação',
    }
  ];

  if (disciplines.length === 0) return (
    <>
      <h1 className="text-3xl">disciplinas</h1>
      <p className="mt-5">Nenhum disciplina encontrado.</p>
    </>
  )

  return (
    <>
      <div className="flex items-center justify-between">
        <h1 className="text-3xl">disciplinas</h1>
        <Link to="/disciplina/create" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">+ adicionar</Link>
      </div>

      <Search />

      <div className="flex flex-col">
        <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
            <div className="overflow-hidden">
              <table className="min-w-full text-left">
                <thead className="font-medium border-b dark:border-stone-200">
                  <tr>
                    <th scope="col" className="px-6 py-4">nome</th>
                    <th scope="col" className="px-6 py-4">curso</th>
                    <th scope="col" className="px-6 py-4"></th>
                    <th scope="col" className="px-6 py-4"></th>
                  </tr>
                </thead>
                <tbody>
                  {disciplines.map((discipline) => (
                    <tr key={discipline.id} className="border-b dark:border-stone-200">
                      <td className="px-6 py-4 whitespace-nowrap">{discipline.nome}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{discipline.id_curso}</td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <Link to={`/disciplina/${discipline.id}`} className="flex items-center underline"><LiaFileAltSolid />detalhes</Link>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <a className="flex items-center text-red-700 underline"><LiaTrashAltSolid />excluir</a>
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

export function Discipline() {
  const discipline: any = {
    id: 1,
    nome: 'Algortimos e Programação',
    descricao: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, vitae aliquam nis',
    id_curso: 'Ciência da Computação',
  };

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">disciplina</h1>
        <Link to="/disciplina" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <div className="flex justify-around gap-10">
        <ul className="flex-grow">
          {Object.keys(discipline).map((key) => (
            <li key={key} className="w-full py-4 border-b-2 border-opacity-50 border-stone-200">
              <strong>{key}:</strong> {discipline[key]}
            </li>
          ))}
        </ul>

        <div className="flex-1">
          <img src="https://placekitten.com/200/200" alt="Foto do disciplina" />
        </div>
      </div>

    </>
  )
}

export function DisciplineCreate() {
  const [discipline, setDiscipline] = useState({
    nome: '',
    descricao: '',
    id_curso: ''
  });

  function handleChange(event: any) {
    const { name, value } = event.target;
    setDiscipline({ ...discipline, [name]: value });
  }

  function handleSubmit(event: any) {
    event.preventDefault();
    console.log(discipline);
  }

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">adicionar disciplina</h1>
        <Link to="/disciplina" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <form className="grid grid-cols-2 gap-4 mt-5" onSubmit={handleSubmit}>
        <Input label="nome" name="nome" value={discipline.nome} onChange={handleChange} />
        <Input label="curso" name="id_curso" value={discipline.id_curso} onChange={handleChange} />
        <Input label="descricao" name="data_ingresso" value={discipline.descricao} onChange={handleChange} />

        <button className="p-2 mt-5 text-white w-min bg-zinc-900 hover:bg-zinc-700">enviar</button>
      </form>
    </>
  )
}
