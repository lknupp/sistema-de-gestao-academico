import { useEffect, useState } from 'react';
import { LiaBookOpenSolid, LiaBookSolid, LiaBuilding, LiaChalkboardTeacherSolid, LiaGraduationCapSolid, LiaUserGraduateSolid } from 'react-icons/lia';
import { IconContext } from 'react-icons';
import { Outlet, Link } from 'react-router-dom';
import {SearchField, Label, Input as AriaInput, Button} from 'react-aria-components';

export function App() {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <main className="m-5 full">
        <Outlet />
      </main>
    </div>
  )
}

export function Search() {
  return (
    <SearchField>
      <AriaInput />
      <Button>✕</Button>
    </SearchField>
  )
}

export function Input({ label, name, value, onChange }: { label: string, name: string, value: string, onChange: any }) {
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={name}>{label}</label>
      <input className="bg-zinc-900" type="text" name={name} id={name} value={value} onChange={onChange} />
    </div>
  )
}

function Sidebar() {
  const items = [
    {
      name: 'professor',
      icon: <LiaChalkboardTeacherSolid />
    },
    {
      name: 'aluno',
      icon: <LiaUserGraduateSolid />
    },
    {
      name: 'curso',
      icon: <LiaGraduationCapSolid />
    },
    {
      name: 'disciplina',
      icon: <LiaBookOpenSolid />
    },
    {
      name: 'campus',
      icon: <LiaBuilding />
    },
    {
      name: 'oferta',
      icon: <LiaBookSolid />
    }
  ];

  return (
    <aside className="p-4 w-52 bg-zinc-900">
      <h2 className="mb-6 text-lg font-bold"><a href="/">sistema de gestão acadêmica</a></h2>
      <ul className="flex flex-col gap-2">
        {items.map((item) => <SidebarItem name={item.name} icon={item.icon} />)}
      </ul>
    </aside>
  )
}

function SidebarItem({ name, icon }: { name: string, icon: JSX.Element }) {
  return (
    <li key={name}>
      <Link className="relative flex items-center w-full gap-2 py-1 pl-2 transition ease-in-out rounded-sm cursor-pointer hover:bg-zinc-300 hover:text-stone-800" to={`/${name}`}>
        <IconContext.Provider value={{ size: '1.5em' }}>
          {icon}
        </IconContext.Provider>
        {name}
      </Link>
    </li>
  )
}

export function Home() {
  return (
    <>
      <h1 className="mb-4 text-4xl">bem-vindo ao sistema de gestão acadêmica</h1>
      <p className="text-2xl">selecione uma opção no menu lateral.</p>
    </>
  )
}