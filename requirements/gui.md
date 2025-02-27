# Графический интерфейс приложения

## Легенда

- Пользовательские истории - User Stories (US) и порядковый номер
- Функциональные требования - Functional Requirements (FR) и порядковый номер
- Элементы графического интерфейса именуются аббревиатурами (e.g. DTP = Diagram Tree Panel) для удобства их упоминания.

## US и FR
---

### US001
Как бизнес-аналитик, я хочу видеть все заведенные в систему диаграммы с их взаимосвязями, чтобы быстро фокусироваться на нужной.
Нужно повторить типовой GIU ARIS и иной ARIS-подобной системы: [Интерфейс ARIS](https://github.com/bpmbpm/doc/blob/main/Project/SemanticBPM/design/mainGUI.md)

#### FR001
Вывести дерево диаграмм бизнес-процессов в левую боковую панель интерфейса (DTP). Узлы дерева сворачиваются-разворачиваются по клику на иконку свертки. При клике по имени диаграммы, происходит вывод этой диаграммы в основную панель интерфейса.

Немного проговорили про [TreeView, Case1 VADtoTreeView](https://github.com/bpmbpm/doc/blob/main/METAMODEL/SIRIUS/Case1_VADtoTreeView.md)

#### FR002
Реализовать фильтр диаграмм по их типу в виде переключающих кнопок на тулбоксе (DTP_TBX) в DTP.

---
