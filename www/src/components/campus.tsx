import { Link } from "react-router-dom";
import { Input } from "../App";
import { useState } from "react";
import { LiaFileAltSolid, LiaTrashAltSolid } from "react-icons/lia";

export function Campuss() {
  const campuss = [
    {
      id: 1,
      nome: 'Taguatinga',
    },
    {
      id: 2,
      nome: 'Brasília'
    }
  ];

  if (campuss.length === 0) return (
    <>
      <h1 className="text-3xl">campus</h1>
      <p className="mt-5">Nenhum campus encontrado.</p>
    </>
  )

  return (
    <>
      <div className="flex items-center justify-between">
        <h1 className="text-3xl">campus</h1>
        <Link to="/campus/create" className="p-2 mt-2 text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">+ adicionar</Link>
      </div>

      <div className="flex flex-col">
        <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
            <div className="overflow-hidden">
              <table className="min-w-full text-left">
                <thead className="font-medium border-b dark:border-stone-200">
                  <tr>
                    <th scope="col" className="px-6 py-4">nome</th>
                    <th scope="col" className="px-6 py-4"></th>
                    <th scope="col" className="px-6 py-4"></th>
                  </tr>
                </thead>
                <tbody>
                  {campuss.map((campus) => (
                    <tr key={campus.id} className="border-b dark:border-stone-200">
                      <td className="px-6 py-4 whitespace-nowrap">{campus.nome}</td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <Link to={`/campus/${campus.id}`} className="flex items-center underline"><LiaFileAltSolid />detalhes</Link>
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

export function Campus() {
  const campus: any = {
    id: 1,
    nome: 'Ciência da Computação'
  };

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">campus</h1>
        <Link to="/campus" className="p-2 mt-2 text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <div className="flex justify-around gap-10">
        <ul className="flex-grow">
          {Object.keys(campus).map((key) => (
            <li key={key} className="w-full py-4 border-b-2 border-opacity-50 border-stone-200">
              <strong>{key}:</strong> {campus[key]}
            </li>
          ))}
        </ul>

        <div className="flex-1">
          <img src="https://placekitten.com/200/200" alt="Foto do campus" />
        </div>
      </div>

    </>
  )
}

export function CampusCreate() {
  const [campus, setCampus] = useState({
    nome: ''
  });

  function handleChange(event: any) {
    const { name, value } = event.target;
    setCampus({ ...campus, [name]: value });
  }

  function handleSubmit(event: any) {
    event.preventDefault();
    console.log(campus);
  }

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">adicionar campus</h1>
        <Link to="/campus" className="p-2 mt-2 text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <form className="grid grid-cols-2 gap-4 mt-5" onSubmit={handleSubmit}>
        <Input label="nome" name="nome" value={campus.nome} onChange={handleChange} />
      </form>

      <button className="p-2 mt-5 text-white w-min bg-zinc-900 hover:bg-zinc-700">enviar</button>
    </>
  )
}
