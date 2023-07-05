# Diagrama de Esquema

+ Aluno(**id_aluno**, nome, sobrenome, cpf, sexo, raca, data_ingresso, id_curso);

+ Professor(**id_prof**, nome, sobrenome, cpf, sexo, raca, data_contratacao, departamento, salario, id_curso);

+ Endereço(**id_endereco**, logradouro, local, numero, cep, tipo);

+ Telefone(**id_telefone**, id_pessoa, cod_pais, ddd, num_telefone);

+ Cursa(**id_cursa**, id_aluno, id_oferta, semestre, ano, nota, presenca);

+ Ministra(**id_professor**, **id_oferta**)

+ Curso(**id_curso**, nome, campus);

+ Disciplina(**id_disciplina**, id_curso, nome, descricao);

+ PreRequisitos(**id_prerequisito**, **id_disciplina**);

+ Oferta(**id_oferta**, **semestre**, **ano**, **id_disciplina**, id_sala, id_periodo);

+ Periodo(**id_periodo**);

+ Horario(**id_horario**, id_periodo, dia, hora_inicial, hora_final);

+ Sala(**id_sala**, predio, sala, capacidade);

+ ModeloEquipamento(**id_modelo**, nome, marca);

+ Equipamento(**id_equipamento**, id_modelo, id_sala, estado, data_aquisicao);

