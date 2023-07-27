import { Link } from "react-router-dom";
import { Input } from "../App";
import { useState } from "react";
import { LiaFileAltSolid, LiaTrashAltSolid } from "react-icons/lia";

export function Students() {
  const students = [
    {
      id: 1,
      nome: 'João',
      sobrenome: 'Silva',
      data_nascimento: '01/01/2000',
      cpf: '000.000.000-00',
      sexo: 'Masculino',
      id_telefone: '0000-0000',
      id_endereco: 'Rua 1, 1',
      raca: 'Branco',
      id_curso: 'Ciência da Computação',
      data_ingresso: '01/01/2020'
    },
    {
      id: 2,
      nome: 'Maria',
      sobrenome: 'Silva',
      data_nascimento: '01/01/2000',
      cpf: '000.000.000-00',
      sexo: 'Feminino',
      id_telefone: '0000-0000',
      id_endereco: 'Rua 1, 1',
      raca: 'Branco',
      id_curso: 'Ciência da Computação',
      data_ingresso: '01/01/2020'
    }
  ];

  if (students.length === 0) return (
    <>
      <h1 className="text-3xl">alunos</h1>
      <p className="mt-5">Nenhum aluno encontrado.</p>
    </>
  )

  return (
    <>
      <div className="flex items-center justify-between">
        <h1 className="text-3xl">alunos</h1>
        <Link to="/aluno/create" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">+ adicionar</Link>
      </div>

      <div className="flex flex-col">
        <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
            <div className="overflow-hidden">
              <table className="min-w-full text-left">
                <thead className="font-medium border-b dark:border-stone-200">
                  <tr>
                    <th scope="col" className="px-6 py-4">nome</th>
                    <th scope="col" className="px-6 py-4">curso</th>
                    <th scope="col" className="px-6 py-4">data de ingresso</th>
                    <th scope="col" className="px-6 py-4"></th>
                    <th scope="col" className="px-6 py-4"></th>
                  </tr>
                </thead>
                <tbody>
                  {students.map((student) => (
                    <tr key={student.id} className="border-b dark:border-stone-200">
                      <td className="px-6 py-4 whitespace-nowrap">{student.nome} {student.sobrenome}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{student.id_curso}</td>
                      <td className="px-6 py-4 whitespace-nowrap">{student.data_ingresso}</td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <Link to={`/aluno/${student.id}`} className="flex items-center underline"><LiaFileAltSolid />detalhes</Link>
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

export function Student() {
  const student: any = {
    id: 1,
    nome: 'João',
    sobrenome: 'Silva',
    data_nascimento: '01/01/2000',
    cpf: '000.000.000-00',
    sexo: 'Masculino',
    id_telefone: '0000-0000',
    id_endereco: 'Rua 1, 1',
    raca: 'Branco',
    id_curso: 'Ciência da Computação',
    data_ingresso: '01/01/2020'
  };

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">aluno</h1>
        <Link to="/aluno" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <div className="flex justify-around gap-10">
        <ul className="flex-grow">
          {Object.keys(student).map((key) => (
            <li key={key} className="w-full py-4 border-b-2 border-opacity-50 border-stone-200">
              <strong>{key}:</strong> {student[key]}
            </li>
          ))}
        </ul>

        <div className="flex-1">
          <img src="https://placekitten.com/200/200" alt="Foto do aluno" />
        </div>
      </div>

    </>
  )
}

export function StudentCreate() {
  const [student, setStudent] = useState({
    nome: '',
    sobrenome: '',
    data_nascimento: '',
    cpf: '',
    sexo: '',
    id_telefone: '',
    id_endereco: '',
    raca: '',
    id_curso: '',
    data_ingresso: ''
  });

  function handleChange(event: any) {
    const { name, value } = event.target;
    setStudent({ ...student, [name]: value });
  }

  function handleSubmit(event: any) {
    event.preventDefault();
    console.log(student);
  }

  return (
    <>
      <div className="flex items-center justify-between mb-5">
        <h1 className="text-3xl">adicionar aluno</h1>
        <Link to="/aluno" className="p-2 mt-2 transition ease-in-out rounded-sm text-stone-200 w-fit bg-zinc-900 hover:bg-zinc-700">voltar</Link>
      </div>

      <form className="grid grid-cols-2 gap-4 mt-5" onSubmit={handleSubmit}>
        <Input label="nome" name="nome" value={student.nome} onChange={handleChange} />
        <Input label="sobrenome" name="sobrenome" value={student.sobrenome} onChange={handleChange} />
        <Input label="data de nascimento" name="data_nascimento" value={student.data_nascimento} onChange={handleChange} />
        <Input label="cpf" name="cpf" value={student.cpf} onChange={handleChange} />
        <Input label="sexo" name="sexo" value={student.sexo} onChange={handleChange} />
        <Input label="telefone" name="id_telefone" value={student.id_telefone} onChange={handleChange} />
        <Input label="endereço" name="id_endereco" value={student.id_endereco} onChange={handleChange} />
        <Input label="raça" name="raca" value={student.raca} onChange={handleChange} />
        <Input label="curso" name="id_curso" value={student.id_curso} onChange={handleChange} />
        <Input label="data de ingresso" name="data_ingresso" value={student.data_ingresso} onChange={handleChange} />

        <button className="p-2 mt-5 text-white w-min bg-zinc-900 hover:bg-zinc-700">enviar</button>
      </form>
    </>
  )
}
