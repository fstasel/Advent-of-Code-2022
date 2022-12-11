from enum import Enum
import math


class OpType(Enum):
    VARIABLE = 1
    LITERAL = 2


f = open('input.txt', 'r')
data = f.read().split('\n\n')
nmonkey = len(data)

monkeys = []
for d in data:
    md = d.splitlines()
    items = [int(i) for i in md[1].split(':')[1].split(',')]
    opdata = md[2].split('new = old ')
    op = opdata[1][0]
    if opdata[1][2:] == 'old':
        operand = 0
        operand_type = OpType.VARIABLE
    else:
        operand = int(md[2].split('new = old ')[1][2:])
        operand_type = OpType.LITERAL
    rule = int(md[3].split('by ')[1])
    truemonkey = int(md[4].split('monkey ')[1])
    falsemonkey = int(md[5].split('monkey ')[1])
    monkeys.append({'items': items, 'operator': op, 'operand': operand,
                   'operand_type': operand_type, 'rule': rule, 'true': truemonkey, 'false': falsemonkey, 'inspect': 0})
print(monkeys)

for _ in range(20):
    for i in range(nmonkey):
        monkeys[i]['inspect'] += len(monkeys[i]['items'])
        for worry in monkeys[i]['items']:
            if monkeys[i]['operand_type'] == OpType.VARIABLE:
                op = worry
            else:
                op = monkeys[i]['operand']
            if monkeys[i]['operator'] == '+':
                worry += op
            else:
                worry *= op
            worry //= 3
            if worry % monkeys[i]['rule'] == 0:
                monkeys[monkeys[i]['true']]['items'].append(worry)
            else:
                monkeys[monkeys[i]['false']]['items'].append(worry)
        monkeys[i]['items'].clear()

ins = [m['inspect'] for m in monkeys]
ins.sort(reverse=True)
mb = ins[0] * ins[1]
print(mb)

# part 2

monkeys = []
for d in data:
    md = d.splitlines()
    items = [[int(i)] * nmonkey for i in md[1].split(':')[1].split(',')]
    opdata = md[2].split('new = old ')
    op = opdata[1][0]
    if opdata[1][2:] == 'old':
        operand = 0
        operand_type = OpType.VARIABLE
    else:
        operand = int(md[2].split('new = old ')[1][2:])
        operand_type = OpType.LITERAL
    rule = int(md[3].split('by ')[1])
    truemonkey = int(md[4].split('monkey ')[1])
    falsemonkey = int(md[5].split('monkey ')[1])
    monkeys.append({'items': items, 'operator': op, 'operand': operand,
                   'operand_type': operand_type, 'rule': rule, 'true': truemonkey, 'false': falsemonkey, 'inspect': 0})
print(monkeys)


for _ in range(10000):
    for i in range(nmonkey):
        monkeys[i]['inspect'] += len(monkeys[i]['items'])
        for worry in monkeys[i]['items']:
            if monkeys[i]['operand_type'] == OpType.VARIABLE:
                if monkeys[i]['operator'] == '+':
                    worry = [(worry[k] + worry[k]) % monkeys[k]['rule']
                             for k in range(nmonkey)]
                else:
                    worry = [(worry[k] * worry[k]) % monkeys[k]['rule']
                             for k in range(nmonkey)]
            else:
                op = monkeys[i]['operand']
                if monkeys[i]['operator'] == '+':
                    worry = [(worry[k] + op) % monkeys[k]['rule']
                             for k in range(nmonkey)]
                else:
                    worry = [(worry[k] * op) % monkeys[k]['rule']
                             for k in range(nmonkey)]
            if worry[i] % monkeys[i]['rule'] == 0:
                monkeys[monkeys[i]['true']]['items'].append(worry)
            else:
                monkeys[monkeys[i]['false']]['items'].append(worry)
        monkeys[i]['items'].clear()

ins = [m['inspect'] for m in monkeys]
ins.sort(reverse=True)
mb = ins[0] * ins[1]
print(mb)
