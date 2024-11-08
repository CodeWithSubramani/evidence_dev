---
title: Home Page
---

```sql users
  select
  cast(created_at as DATE) as registered_date,
  count(*) as count_of_registered_users from iam.users
  group by all
  order by 1 desc
  limit 5;
```

```sql total_users
  select
  count(*) as count_of_total_users
  from iam.users
  group by all
  order by 1 desc
  limit 5;
```

```sql avg_users_per_day
  select avg(count_of_registered_users) as avg_users_per_day from(
  select
  cast(created_at as DATE) as registered_date,
  count(*) as count_of_registered_users from iam.users
  group by all)
```

<br/>
<br/>
<br/>

<center>
<Grid cols=2>

<BigValue data={total_users} value=count_of_total_users/>
<BigValue data={avg_users_per_day} value=avg_users_per_day/>

</Grid>
</center>

<DataTable data={users}/>
