import { useRouteError } from "react-router-dom";
import { BiError } from "react-icons/bi";

export default function ErrorPage() {
  const error = useRouteError() as { status?: number; statusText?: string; message?: string };
  console.error(error);

  return (
    <div className="flex flex-col items-center justify-center h-screen gap-5">
      <h1 className="flex flex-col items-center justify-center text-5xl font-bold"><BiError /> <span>{`erro ${error.status}`}</span></h1>
      <p className="text-xl text-stone-400">
        <i>{`${error.statusText}` || error.message}</i>
      </p>
    </div>
  );
}