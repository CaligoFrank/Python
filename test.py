def show_notes_for_selected_patient(*args):
    selected_item = tvPatient.selection()
    if not selected_item:
        return
    
    patient_id = tvPatient.item(selected_item[0], 'values')[0]
    
    for item in tvNotes.get_children():
        tvNotes.delete(item)
    
    conn = sqlite3.connect(path + "notes.db")
    c = conn.cursor()
    c.execute("SELECT date, notes FROM patient_notes WHERE patient_id = ? ORDER BY date", (patient_id,))
    notes = c.fetchall()
    conn.close()
    
    for note in notes:
        tvNotes.insert("", 'end', values=(patient_id, '', '', note[1]))