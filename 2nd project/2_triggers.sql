-- Trigger function to update historique_item_price
CREATE OR REPLACE FUNCTION update_historique_item_price()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO historique_item_price (item_id, price, date_debut, date_fin)
    VALUES (NEW.id, NEW.cout, OLD.last_date_price_modified, CURRENT_DATE);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to fire when the price of an item is updated
CREATE TRIGGER update_item_price_trigger
AFTER UPDATE OF cout ON item
FOR EACH ROW
EXECUTE FUNCTION update_historique_item_price();

/* ****************************************************************************** */
-- Trigger function to recalculate item price
CREATE OR REPLACE FUNCTION recalculate_item_price()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE item
    SET last_date_price_modified = CURRENT_DATE,
        cout = (item.cout * item.qnt + NEW.qnt * NEW.price) / (item.qnt + NEW.qnt),
        qnt = item.qnt + NEW.qnt
    WHERE id = NEW.item_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to fire when a new achat record is added
CREATE TRIGGER update_item_price_trigger
AFTER INSERT ON achat
FOR EACH ROW
EXECUTE FUNCTION recalculate_item_price();

/* ****************************************************************************** */
-- Trigger function to decrease quantity in item table
CREATE OR REPLACE FUNCTION decrease_item_quantity()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE item
    SET qnt = qnt - NEW.qnt
    WHERE id = NEW.item_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to fire when a row is inserted or updated in project_items
CREATE TRIGGER decrease_item_quantity_trigger
AFTER INSERT OR UPDATE ON project_items
FOR EACH ROW
EXECUTE FUNCTION decrease_item_quantity();

-- Trigger function to increase quantity in item table
CREATE OR REPLACE FUNCTION increase_item_quantity()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE item
    SET qnt = qnt + OLD.qnt
    WHERE id = OLD.item_id;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- Trigger to fire when a row is deleted from project_items
CREATE TRIGGER increase_item_quantity_trigger
AFTER DELETE ON project_items
FOR EACH ROW
EXECUTE FUNCTION increase_item_quantity();
