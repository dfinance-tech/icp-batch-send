import os

cmd = "dfx ledger --network ic transfer ADDRESS --amount AMOUNT --memo MEMO"

def transfer(to, amount, memo):
    c = cmd.replace('ADDRESS', to).replace('AMOUNT', amount).replace('MEMO', memo)
    # print(c)
    os.system(c)

with open('addresses.txt', 'r') as f:
    count = 0
    for line in f:
        info = line.split()
        if len(info) != 2:
            continue
        addr = info[0]
        amount = info[1]
        memo = str(count)
        print('transferring', amount, 'ICP to', addr)
        transfer(addr, amount, memo)
        count += 1
