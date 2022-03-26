class SqlConfigs(object):
    db_name = 'forward_rate'
    insert_params = ['date', 'libor_rate', 'sofr_rate']

    create_table='''
        CREATE TABLE IF NOT EXISTS rates
        (
            [date] TEXT UNIQUE PRIMARY KEY, 
            [libor_rate] TEXT, 
            [sofr_rate] NUMERIC
        )
    '''

    insert_items='''
        INSERT OR IGNORE INTO rates (date, libor_rate, sofr_rate) VALUES(?, ?, ?)
    '''

    get_items='''
        SELECT date, libor_rate, sofr_rate, cast(strftime('%d', date) as INTEGER)-cast(strftime('%d', ?) as INTEGER) diff
        FROM rates
        WHERE date<=? AND
        diff IN (
        SELECT min(cast(strftime('%d', date) as INTEGER)-cast(strftime('%d', ?) as INTEGER)) minDuration
        FROM rates)
    '''