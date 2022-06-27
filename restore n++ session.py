import os
import os.path as osp

def write_to_file(output):
	path = os.getcwd() + '\\restored_session.xml'

	with open(path, 'w') as fileout:
		fileout.write(output)



def main():
	npp_path = osp.join(osp.expandvars('%APPDATA%'), 'Notepad++', 'backup')
	session_txt = '<?xml version="1.0" encoding="UTF-8" ?> ' \
		'<NotepadPlus>' \
		'<Session activeView="0">' \
		'<mainView activeIndex="0">'
	for fn in sorted(os.listdir(npp_path), key=lambda fn: fn.split('@')[1]):
		name = fn.split('@')[0]
		session_txt = session_txt + '<File firstVisibleLine="0" xOffset="0" scrollWidth="64" ' \
		'startPos="8" endPos="8" selMode="0" lang="Normal Text" ' \
		'encoding="-1" userReadOnly="no" filename="{name}" ' \
		'backupFilePath="{npp_path}\{fn}" originalFileLastModifTimestamp="0" ' \
		'originalFileLastModifTimestampHigh="0" ' \
		'mapFirstVisibleDisplayLine="-1" mapFirstVisibleDocLine="-1" ' \
		'mapLastVisibleDocLine="-1" mapNbLine="-1" mapHigherPos="-1" ' \
		'mapWidth="-1" mapHeight="-1" mapKByteInDoc="0" ' \
		'mapWrapIndentMode="-1" mapIsWrap="no" />'.format(
			name=name, npp_path=npp_path, fn=fn)

	session_txt = session_txt + '</mainview>' \
		'<subView activeIndex="0" />' \
		'</Session>' \
		'</NotepadPlus>'

	write_to_file(session_txt)


if __name__ == '__main__':
	main()

