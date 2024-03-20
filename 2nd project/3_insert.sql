select * from item;

select * from achat;

select * from historique_item_price;

select * from division;

select * from pole;

select * from projet;

select * from project_items;



/*
	insert into item (nom, cout, last_date_price_modified ) values ('item1', 0, null);

	insert into achat (item_id, qnt, price ) values (2, 10, 25);

	update item set cout = 25, qnt = 10 where id = 1

	delete from item
	
	-- Insert constant Divisions
	insert into division (nom, libelle ) values ('DDE', 'Déssalement');
	insert into division (nom, libelle ) values ('DTH', 'Hydraulique');
	insert into division (nom, libelle ) values ('DTE', 'HydroCarbure');
	
	-- Insert Poles
	insert into pole (nom, libelle, division_id  ) values ('H48', 'Fouka', 1);
	insert into pole (nom, libelle, division_id ) values ('HE01', '', 1);
	insert into pole (nom, libelle, division_id ) values ('C01', '', 3);
	insert into pole (nom, libelle, division_id ) values ('C06', '', 3);
	insert into pole (nom, libelle, division_id ) values ('H31', '', 2);
	insert into pole (nom, libelle, division_id ) values ('H36', '', 2);
	insert into pole (nom, libelle, division_id ) values ('H56', '', 2);
	
	-- Insert Projet
	insert into public.projet (pole_id, budget, date_ouverture, intitule) 
		values (1, 250000, CURRENT_DATE, 'dessalement de l''eau de mere')
*/


insert into public.project_items (item_id, price, qnt, date, project_id ) 
values (2, 35, 3, CURRENT_DATE, 1)



