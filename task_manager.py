import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(tasks):
    title = input("Digite o título da tarefa: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("✅ Tarefa adicionada com sucesso!")
    else:
        print("❌ Título inválido.")


def list_tasks(tasks):
    if not tasks:
        print("📭 Nenhuma tarefa cadastrada.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✔ Concluída" if task["done"] else "⏳ Pendente"
        print(f"{index}. {task['title']} - {status}")


def complete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Digite o número da tarefa concluída: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("🎉 Tarefa marcada como concluída!")
    except (ValueError, IndexError):
        print("❌ Opção inválida.")


def remove_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Digite o número da tarefa para remover: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑 Tarefa '{removed['title']}' removida!")
    except (ValueError, IndexError):
        print("❌ Opção inválida.")


def menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def main():
    tasks = load_tasks()

    while True:
        menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            add_task(tasks)
        elif option == "2":
            list_tasks(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            remove_task(tasks)
        elif option == "0":
            print("👋 Saindo do programa...")
            break
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()