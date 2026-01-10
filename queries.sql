select a.username as 'follower', b.username as 'followed'
from user a
join followers f on a.id = f.follower_id
join user b on b.id = f.followed_id
where a.id = 1;

# select a.username as 'follower', b.username as 'followed', p.body as 'my post'
# from user a
# join followers f on a.id = f.follower_id
# join user b on b.id = f.followed_id
# join post p on a.id = p.user_id;

# # just my posts
# select u.username as 'author', p.body as 'my post'
# from user u
# join post p on u.id = p.user_id
# where u.id = 1;

# # my followed posts
# select u.username as 'follower', p.body as 'their post'
# from user u
# join followers f on u.id = f.followed_id
# join post p on u.id = p.user_id
# where f.follower_id = 1;

select u.username as 'author', p.body as 'my post'
from user u
join followers f on u.id = f.followed_id
join post p on u.id = p.user_id
left join (
select u.username as 'follower', p.body as 'their post', f.follower_id
from user u
join followers f on u.id = f.followed_id
join post p on u.id = p.user_id) t2
on u.id = t2.follower_id
where u.id = 1;
