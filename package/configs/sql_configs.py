class SqlConfigs(object):
    db_name = 'forward_rate'
    select_params = ['date']
    insert_params = ['date', 'libor_rate', 'sofr_rate']
    update_params = ['libor_rate', 'sofr_rate', 'date']
    query_cols = ['date', 'libor_rate', 'sofr_rate', 'diff']

    create_table='''
        CREATE TABLE IF NOT EXISTS rates
        (
            [date] TEXT UNIQUE PRIMARY KEY, 
            [libor_rate] NUMERIC, 
            [sofr_rate] NUMERIC
        )
    '''

    select_items='''
        SELECT date, libor_rate, sofr_rate FROM rates WHERE date=?
    '''

    insert_items='''
        INSERT OR IGNORE INTO rates (date, libor_rate, sofr_rate) VALUES(?, ?, ?)
        
    '''

    update_items='''
        UPDATE rates SET libor_rate=?, sofr_rate=? WHERE date=?
    '''

    get_items='''
        SELECT date, libor_rate, sofr_rate, cast(strftime('%d', date) as INTEGER)-cast(strftime('%d', ?) as INTEGER) diff
        FROM rates
        WHERE date<=? AND
        diff IN (
        SELECT min(cast(strftime('%d', date) as INTEGER)-cast(strftime('%d', ?) as INTEGER)) minDuration
        FROM rates)
    '''