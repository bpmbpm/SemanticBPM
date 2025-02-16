## Определим для начала понятия

Это первое предложение, ожидаю что это должно ещё много раз 
пересматриваться и уточняться.

[Брейншторм в GPT](https://chatgpt.com/share/67afd750-4098-8004-96b8-396059c26905)

### BusinessProcess Бизнес процесс

Некий подкласс События/Процесса (occurent) или process в SUMO

Процесс с дополительной характеристикой связанной с 
экономической, организационной или стратегической  Utility (полезность)
его результата.

### Utility полезность

Возможность сущности генерировать ценность 
удовлетворяющую потребность или генерировать достижение успеха.

###  OrganizationalUtility  организационная полезность 

Понятие означающее улучшение (а теперь что такое улучшение )
эффективности совместного действия многих активных сущностей
(которые образуют организацию)

###  EconomicUtility экономическая полезность

Измеряемая экономическая выгода

The measurable financial benefit a process provides, such as cost savings, increased revenue, or improved return on investment (ROI).
        Key Characteristics:

Cost Reduction: Lowers operational expenses through process optimization.
Revenue Enhancement: Boosts sales or market share by improving service delivery.
ROI Improvement: Offers quantifiable gains that justify the process investment.
        Example: A supply chain process that reduces inventory costs and improves delivery speed, thereby increasing profit margins.

###  StrategicUtility экономическая полезность

The contribution of a process to an organization’s long-term strategic goals and competitive positioning, supporting future growth and market differentiation.
        Key Characteristics:

Alignment with Vision: Directly supports long-term strategic objectives.
Innovation and Differentiation: Creates unique capabilities that set the organization apart.
Market Adaptability: Enhances the ability to respond to market changes and seize emerging opportunities.
        Example: A digital transformation process that redefines business models, opens new market opportunities, and secures a sustainable competitive advantage.

## upd1 bpmbpm
Бизнес-процесс = процесс

Ссылки:
- [В толковый словарь Business Process Management: Бизнес-функция vs Бизнес-процесс](https://habr.com/ru/users/itGuevara/articles/)
- [ARIS Method_Manual.pdf, п 4.1.1.1 Function tree, стр. 12](https://github.com/bpmbpm/doc/blob/main/BPM/ARIS/SCHEER/BASE/10-0sr6_Method_Manual.pdf)
- [из Надежность в процессах](https://habr.com/ru/articles/844992/):
_В общем случае, синонимы: делание, процесс, операция, функция, действие, активность (activity)_
<img src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/551/150/be3/551150be35284815480f75811b2129f0.png" width="600" />
- Упрощенно, процес = математическая функция. Математическая функция (процесс) имеет значение (результат процесса), аргументы (ресурсы, включая входы, инструменты, исполнителя) и формулу (алгоритм процсса). Можно усложниять, что на выполнение (вычисдение) функции вдияют внешние и внутренние воздействующие факторы, т.е. углубляться в теорию вероятности (надежности), но в рамках нашего проекта такое усложнение излишне.   

Важно: Мы различаем BPM: один маркетинговый - где много "умных и загадочных" терминов, второй математический, где понятия "очищены" от маргетинговой и наукообраной шелухи. Онтологию "процесс" = "бизнес-процесс" в первую очередь (в рамках этого проекта) будем строить под математическое определение процесса, т.е. как класическую функцию преобразования. Отдельно можно онтологизировать маркетинговые интерпретации "бизнес-процесс", но тогда это нужно явно оговаривать. 

Термины Бизнес-функция, бизнес-способность и т.п. если не сможем зафиксировать (определить) математически (строго), то отнесем их к "маркетинговому BPM". В EKG должно быть без наукообразия, а четкая "бухгалтерская" / математическая интерпретация сущностей. Фактически EKG можно расматривать как аналог "Главной книги" в бухучете. Во всяком случае ровно так же строго нужно подходить к определениям (составляющим бухучета, включая план счет, правила, включая правило двойной записи).

Для начала можно определить "процесс" исключительно под его формализацию нотацией VAD (узкий термин, процесс в "узком" смысле слова). Можно так и назвать "VAD-процесс" - как подкласс "бизнес-процесс", см [широкое определение](https://github.com/bpmbpm/SemanticBPM/blob/main/ontology/smer44/concepts.md#upd1-bpmbpm). Также см. [примеры VAD](https://github.com/bpmbpm/SemanticBPM/blob/main/docs/VAD/aboutVAD.md)
