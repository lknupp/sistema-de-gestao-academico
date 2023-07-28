import { Link } from "react-router-dom";
import { Input, Search } from "../App";
import { useState } from "react";
import { LiaFileAltSolid, LiaTrashAltSolid } from "react-icons/lia";

export function Professors() {
  const professors = [
    {
      id: 1,
      nome: 'João',
      sobrenome: 'Silva',
      cpf: '000.000.000-00',
      sexo: 'Masculino',
      id_telefone: '0000-0000',
      id_endereco: 'Rua 1, 1',
      raca: 'Branco',
      id_curso: 'Ciência da Computação',
      dataContratacao: '01/01/2020',
      departamento: 'Departamento 1',
      salario: 'R$ 1.000,00'
    },
    {
      id: 2,
      nome: 'Maria',
      sobrenome: 'Silva',
      cpf: '000.000.000-00',
      sexo: 'Feminino',
      id_telefone: '0000-0000',
      id_endereco: 'Rua 1, 1',
      raca: 'Branco',
      id_curso: 'Ciência da Computação',
      dataContratacao: '01/01/2020',
      departamento: 'Departamento 1',
      salario: 'R$ 1.000,00'
    }
  ];

  if (professors.length === 0) return (
    <>
      <h1 className="text-3xl">professores</h1>
      <p className="mt-5">Nenhum professor encontrado.</p>
    </>
  )

  return (
    <>
      <div className="flex items-center justify-between">
        <h1 className="text-3xl">professores</h1>
        <Link to="/professor/create" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">+ adicionar</Link>
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
                    <th scope="col" className="px-6 py-4">departamento</th>
                    <th scope="col" className="px-6 py-4">data de contratação</th>
                    <th scope="col" className="px-6 py-4"></th>
                    <th scope="col" className="px-6 py-4"></th>
                  </tr>
                </thead>
                <tbody>
                  {professors.map((professor) => (
                    <tr key={professor.id} className="border-b dark:border-stone-200">
                      <td className="px-6 py-4 whitespace-nowrap">{professor.nome} {professor.sobrenome}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{professor.departamento}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{professor.dataContratacao}</td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <Link to={`/professor/${professor.id}`} className="flex items-center underline"><LiaFileAltSolid />detalhes</Link>
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

export function Professor() {
  const professor: any = {
    id: 2,
    nome: 'Maria',
    sobrenome: 'Silva',
    cpf: '000.000.000-00',
    sexo: 'Feminino',
    id_telefone: '0000-0000',
    id_endereco: 'Rua 1, 1',
    raca: 'Branco',
    id_curso: 'Ciência da Computação',
    dataContratacao: '01/01/2020',
    departamento: 'Departamento 1',
    salario: 'R$ 1.000,00'

  };

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">professor</h1>
        <Link to="/professor" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <div className="flex justify-around gap-10">
        <ul className="flex-grow">
          {Object.keys(professor).map((key) => (
            <li key={key} className="w-full py-4 border-b-2 border-opacity-50 border-stone-200">
              <strong>{key}:</strong> {professor[key]}
            </li>
          ))}
        </ul>

        <div className="flex-1">
          <img src="https://placekitten.com/200/200" alt="Foto do professor" />
        </div>
      </div>

    </>
  )
}

export function ProfessorCreate() {
  const [professor, setProfessor] = useState({
    nome: '',
    sobrenome: '',
    cpf: '',
    sexo: '',
    id_telefone: '',
    id_endereco: '',
    raca: '',
    id_curso: '',
    dataContratacao: '',
    departamento: '',
    salario: ''
  });

  function handleChange(event: any) {
    const { name, value } = event.target;
    setProfessor({ ...professor, [name]: value });
  }

  function handleSubmit(event: any) {
    event.preventDefault();
    console.log(professor);
  }

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">adicionar professor</h1>
        <Link to="/professor" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <form className="grid grid-cols-2 gap-4 mt-5" onSubmit={handleSubmit}>
        <Input label="nome" name="nome" value={professor.nome} onChange={handleChange} />
        <Input label="sobrenome" name="sobrenome" value={professor.sobrenome} onChange={handleChange} />
        <Input label="cpf" name="cpf" value={professor.cpf} onChange={handleChange} />
        <Input label="sexo" name="sexo" value={professor.sexo} onChange={handleChange} />
        <Input label="telefone" name="id_telefone" value={professor.id_telefone} onChange={handleChange} />
        <Input label="endereço" name="id_endereco" value={professor.id_endereco} onChange={handleChange} />
        <Input label="raça" name="raca" value={professor.raca} onChange={handleChange} />
        <Input label="salário" name="salario" value={professor.salario} onChange={handleChange} />
        <Input label="data de contratação" name="dataContratacao" value={professor.dataContratacao} onChange={handleChange} />
        <Input label="departamento" name="departamento" value={professor.departamento} onChange={handleChange} />
        <Input label="curso" name="id_curso" value={professor.id_curso} onChange={handleChange} />
      </form>

      <button className="p-2 mt-5 text-white w-min bg-zinc-900 hover:bg-zinc-700">enviar</button>
    </>
  )
}
