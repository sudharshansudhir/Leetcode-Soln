select n.name,sum(t.amount) as balance from users as n join transactions as t on n.account=t.account group by t.account having sum(t.amount)>10000
