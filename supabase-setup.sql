-- ============================================================
-- Tiger Soul content calendar — asset uploads (run ONCE)
-- Supabase dashboard → SQL Editor → paste all of this → Run
-- Project: werkohszkcytdvljafha
-- ============================================================

-- 1) Public storage bucket for uploaded photos/videos (200 MB per file)
insert into storage.buckets (id, name, public, file_size_limit)
values ('calendar-uploads', 'calendar-uploads', true, 209715200)
on conflict (id) do update set public = true, file_size_limit = 209715200;

-- Anyone can read / upload / delete objects in THIS bucket only
drop policy if exists "cal read"   on storage.objects;
drop policy if exists "cal insert" on storage.objects;
drop policy if exists "cal delete" on storage.objects;
create policy "cal read"   on storage.objects for select using (bucket_id = 'calendar-uploads');
create policy "cal insert" on storage.objects for insert with check (bucket_id = 'calendar-uploads');
create policy "cal delete" on storage.objects for delete using (bucket_id = 'calendar-uploads');

-- 2) Table that remembers which upload belongs to which day
create table if not exists public.calendar_assets (
  id uuid primary key default gen_random_uuid(),
  post_date  text not null,
  url        text not null,
  filename   text,
  path       text,
  is_video   boolean default false,
  created_at timestamptz default now()
);
alter table public.calendar_assets enable row level security;
drop policy if exists "ca read"   on public.calendar_assets;
drop policy if exists "ca insert" on public.calendar_assets;
drop policy if exists "ca delete" on public.calendar_assets;
create policy "ca read"   on public.calendar_assets for select using (true);
create policy "ca insert" on public.calendar_assets for insert with check (true);
create policy "ca delete" on public.calendar_assets for delete using (true);
