import { Link } from "react-router-dom";
import { Input, Search } from "../App";
import { useState } from "react";
import { LiaFileAltSolid, LiaTrashAltSolid } from "react-icons/lia";

export function Offerings() {
  const offerings = [
    {
      id_oferta: 1,
      semestre: 1,
      ano: 2021,
      id_professor: 'João',
      id_disciplina: 'Algoritmos e Programação',
      periodo: 'vespertino'
    },
    {
      id_oferta: 2,
      semestre: 1,
      ano: 2021,
      id_professor: 'José',
      id_disciplina: 'Programação Orientada a Objetos',
      periodo: 'matutino'
    }
  ];

  if (offerings.length === 0) return (
    <>
      <h1 className="text-3xl">ofertas</h1>
      <p className="mt-5">Nenhum oferta encontrado.</p>
    </>
  )

  return (
    <>
      <div className="flex items-center justify-between">
        <h1 className="text-3xl">ofertas</h1>
        <Link to="/oferta/create" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">+ adicionar</Link>
      </div>

      <Search />

      <div className="flex flex-col">
        <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
            <div className="overflow-hidden">
              <table className="min-w-full text-left">
                <thead className="font-medium border-b dark:border-stone-200">
                  <tr>
                    <th scope="col" className="px-6 py-4">disciplina</th>
                    <th scope="col" className="px-6 py-4">ano</th>
                    <th scope="col" className="px-6 py-4">semestre</th>
                    <th scope="col" className="px-6 py-4">professor</th>
                    <th scope="col" className="px-6 py-4">período</th>
                    <th scope="col" className="px-6 py-4"></th>
                    <th scope="col" className="px-6 py-4"></th>
                  </tr>
                </thead>
                <tbody>
                  {offerings.map((offering) => (
                    <tr key={offering.id_oferta} className="border-b dark:border-stone-200">
                      <td className="px-6 py-4 whitespace-nowrap">{offering.id_disciplina}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{offering.ano}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{offering.semestre}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{offering.id_professor}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{offering.periodo}</td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <Link to={`/oferta/${offering.id_oferta}`} className="flex items-center underline"><LiaFileAltSolid />detalhes</Link>
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

export function Offering() {
  const offering: any = {
    id_oferta: 1,
    semestre: 1,
    ano: 2021,
    id_professor: 'João',
    id_disciplina: 'Algoritmos e Programação',
    periodo: 'noturno',
  };

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">oferta</h1>
        <Link to="/oferta" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <div className="flex justify-around gap-10">
        <ul className="flex-grow">
          {Object.keys(offering).map((key) => (
            <li key={key} className="w-full py-4 border-b-2 border-opacity-50 border-stone-200">
              <strong>{key}:</strong> {offering[key]}
            </li>
          ))}
        </ul>

        <div className="flex-1">
          <img src="https://placekitten.com/200/200" alt="Foto do oferta" />
        </div>
      </div>

    </>
  )
}

export function OfferingCreate() {
  const [offering, setOffering] = useState({
    semestre: '',
    ano: '',
    id_professor: '',
    id_disciplina: '',
    periodo: '',
    id_oferta: ''
  });

  function handleChange(event: any) {
    const { name, value } = event.target;
    setOffering({ ...offering, [name]: value });
  }

  function handleSubmit(event: any) {
    event.preventDefault();
    console.log(offering);
  }

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">adicionar oferta</h1>
        <Link to="/oferta" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <form className="grid grid-cols-2 gap-4 mt-5" onSubmit={handleSubmit}>
        <Input label="semestre" name="semestre" value={offering.semestre} onChange={handleChange} />
        <Input label="ano" name="ano" value={offering.ano} onChange={handleChange} />
        <Input label="id_professor" name="id_professor" value={offering.id_professor} onChange={handleChange} />
        <Input label="id_disciplina" name="id_disciplina" value={offering.id_disciplina} onChange={handleChange} />
        <Input label="periodo" name="periodo" value={offering.periodo} onChange={handleChange} />
      </form>

      <button className="p-2 mt-5 text-white w-min bg-zinc-900 hover:bg-zinc-700">enviar</button>
    </>
  )
}
