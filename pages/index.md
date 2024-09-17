---
title: Welcome to Evidence
---

```sql categories
  select
      a.category
  from needful_things.orders as a
  left join duplicate.orders as b
  on a.category=b.category
  group by a.category
```

<DataTable data={categories}/>
