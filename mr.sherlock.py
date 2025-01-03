import requests
from bs4 import BeautifulSoup
import argparse
import time

print("                    0000000000000000000000000000")                                
print("                  00000000000000000000000000000000")                              
print("                 0000000000000000000000000000000000")                            
print("                000000000000000000000000000000000000")                           
print("               00000000000000000000000000000000000000")                           
print("               000000000000000000000000000000000000000")                          
print("              30000000000000000000000000000000000000000")                         
print("               000000000000000000000000000000000000000000")                       
print("               000000000000000000000000000000000000000000000")                    
print("               00000000000000000000000000000000000000000000002")                  
print("               0000000000000000000000000000000000000")                            
print("               000000000000000000000000000000000000006")                          
print("              00000000000000000000000000000000000000000")                         
print("              0000000000000000000000000000000000000000000")                       
print("             000000000000000000000000000000000000000000000")                      
print("            30000000000000000000000000000000000000000000000")                     
print("            00000000000000000000000000000000000000000000000")                     
print("                 90000000000000000000000000000000000000")                         
print("                   000000000000000000000000000000000000")                         
print("                    0000000000000000000000000000000000000000")                    
print("                     000000000000000000000000000000000004600000")                 
print("                     000000000000000000000000000000000       000")                
print("               2000000000000000000000000000000000000008       000")               
print("                000000000000000000000000000000000000005       002   77777")       
print("                 0000000000000000000000000000000047           00   0000000")      
print("                 00000000000000000000000000000                008 20000000")      
print("               000000000000000000000000000000                 000000000000")      
print("              0000000000000000000000000000001                  00000000000")      
print("             0000000000000000000000000000000000000               00000000")       
print("            0000000000000000000000000000000000000000000")                         
print("           0000000000000000000000000000000000000000008")                          
print("          0 instagram: @rafael_cyber1 00000000000000")                             
print("         0 mr.sherlock.py V.1.1 000000000000000000")                               

# Lista de sites
social_media_urls = {
    'Odysee': 'https://odysee.com/@{}',
    'Reddit': 'https://www.reddit.com/user/{}',
    'Medium': 'https://medium.com/@{}',
    'Facebook': 'https://www.facebook.com/{}',
    'GitHub': 'https://github.com/{}',
    'Snapchat': 'https://www.snapchat.com/add/{}',
    'WeChat': 'https://weixin.qq.com/u/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    'Skype': 'https://join.skype.com/invite/{}',
    'Spotify': 'https://open.spotify.com/user/{}',
    'Pinterest': 'https://www.pinterest.com/{}/',
    'YouTube': 'https://www.youtube.com/{}',
    'Twitch': 'https://www.twitch.tv/{}',
    'TikTok': 'https://www.tiktok.com/@{}',
    'Xvideos': 'https://www.xvideos.com/profiles/{}',
    'Xnxx': 'https://www.xnxx.com/profile/{}',
    'Pornhub': 'https://www.pornhub.com/users/{}',
    'FreeCodeCamp': 'https://www.freecodecamp.org/{}',
    'TryHackMe': 'https://tryhackme.com/p/{}',
    'Freelancer': 'https://www.freelancer.com/u/{}',
    'FreelancerBR': 'https://www.freelancer.com.br/u/{}',
    'Privacy': 'https://privacy.com/{}',
    'OnlyFans': 'https://onlyfans.com/{}',
    'GitLab': 'https://gitlab.com/{}',
    'Archive.org': 'https://archive.org/details/@{}',
    'Pr0gramm': 'https://pr0gramm.com/user/{}',
    'Fandom': 'https://www.fandom.com/wiki/User:{}',
    'Interpals': 'https://www.interpals.net/{}',
    'PSNProfiles': 'https://psnprofiles.com/{}',
    'About.me': 'https://about.me/{}',
    'PyPI': 'https://pypi.org/user/{}',
    'Tumblr': 'https://{}.tumblr.com/',
    '9GAG': 'https://9gag.com/u/{}',
    'VK': 'https://vk.com/{}',
    'Flickr': 'https://www.flickr.com/people/{}',
    'YouPic': 'https://youpic.com/photographer/{}',
    'MyAnimeList': 'https://myanimelist.net/profile/{}',
    'Wattpad': 'https://www.wattpad.com/user/{}',
    'MySpace': 'https://myspace.com/{}',
    'Passes': 'https://passes.com/{}',
    'Disqus': 'https://disqus.com/by/{}',
    'Threads': 'https://threads.net/{}',
    'XHamster': 'https://xhamster.com/users/{}',
    'Sharesome': 'https://sharesome.com/{}',
    'YouPorn': 'https://youporn.com/uservids/ph-{}',
    'Chaturbate': 'https://chaturbate.com/{}',
    'BongaCams': 'https://pt.bongacams.com/profile/{}',
    'Tinder': 'https://tinder.com/@{}',
    'LiveJasmin': 'https://livejasmin.com/en/chat/{}',
    '7 Cups': 'https://www.7cups.com/@{}',
    'Apclips': 'https://apclips.com/{}',
    'AdmireMe': 'https://admireme.vip/{}',
    'Airbit': 'https://airbit.com/{}',
    'AllMyLinks': 'https://allmylinks.com/{}',
    'AllThingsWorn':'https://www.allthingsworn.com/{}',
    'AniList': 'https://anilist.co/user/{}/',
    'ArtStation': 'https://www.artstation.com/{}',
    'Blipfoto': 'https://www.blipfoto.com/{}',
    'Blogger': 'https://www.blogger.com/{}',
    'RedTube': 'https://www.redtube.com.br/{}',
    'RoyalCams': 'https://pt.royalcams.com/{}',
    'Shpock': 'https://www.shpock.com/{}',
    'Scribd': 'https://pt.scribd.com/{}',
    'Scratch': 'https://scratch.mit.edu/{}',
    'ImgSrc': 'https://imgsrc.ru/{}',
    'MercadoLivre': 'https://www.mercadolivre.com.br/{}',
    'Note': 'https://note.com/{}',
    'PicsArt': 'https://picsart.com/{}',
    'Cont.ws': 'https://cont.ws/@{}',
    'Estante Virtual': 'https://www.estantevirtual.com.br/busca?editora={}',
    'Kwai': 'https://www.kwai.com/@{}',
    'Disqus': 'https://disqus.com/by/{}/?',
    'Telegram': 'https://t.me/{}',
    'Duolingo': 'https://www.duolingo.com/profile/{}',
    'Hentai City': 'https://www.hentaicity.com/profile/{}',
    'Strip Chat': 'https://stripchat.com/user/{}',
    'Ifunnny': 'https://br.ifunny.co/user/{}',
    'Itch': 'https://itch.io/profile/{}',
    'Etsy': 'https://www.etsy.com/pt/people/{}?ref=l_review',
    'Ludopedia': 'https://ludopedia.com.br/usuario/{}',
    'Viva o Linux': 'https://www.vivaolinux.com.br/~{}',
    'Cursos Alura': 'https://cursos.alura.com.br/user/{}',
    'Guj': 'https://www.guj.com.br/u/{}/summary',
    'Mk Auth': 'https://mk-auth.com.br/members/{}',
    'Forum Elipse': 'https://forum.elipse.com.br/u/{}/summary',
    'Home Assistent': 'https://homeassistantbrasil.com.br/u/{}/summary',
    'Endian Eth0': 'https://endian.eth0.com.br/forums/profile/{}',
    'Vakinha': 'https://www.vakinha.com.br/usuario/{}',
    'Mastodon': 'https://mastodon.social/@{}',
    'Anime Planet': 'https://www.anime-planet.com/users/{}',
    'Bsky': 'https://bsky.app/profile/{}.bsky.social',
    'Live Journal': 'https://{}.livejournal.com/',
    'Deviantart': 'https://www.deviantart.com/{}/gallery',
    'Last': 'https://www.last.fm/pt/user/{}',
    'Veoh': 'https://www.veoh.com/users/{}',
    'Behance': 'https://www.behance.net/{}',
    'Tripadvisor': 'https://www.tripadvisor.com.br/Profile/{}',
    'Polyvore': 'https://polyvore.ch/author/{}/',
    'Kongregate': 'https://www.kongregate.com/accounts/{}',
    'Beebom': 'https://beebom.com/author/{}/',
    'Wikihow': 'https://www.wikihow.com/Author/{}',
    'Laptopmag': 'https://www.laptopmag.com/uk/author/{}',
    'Flip Board': 'https://flipboard.com/@{}',
    'Hackr': 'https://hackr.io/blog/author/{}',
    'Clean': 'https://clean.email/authors/{}',
    'Gravatar': 'https://gravatar.com/{}',
    'Dio': 'https://www.dio.me/users/{}',
    'Sex HD': 'https://www.sexhd.pics/mobile/{}',
    'Blog Bang': 'https://blog.bang.com/author/{}',
    'Bang': 'https://www.bang.com/videos?term={}',
    'Eplay': 'https://www.eplay.com/{}',
    'Eporner': 'https://www.eporner.com/profile/{}',
    'Eyeem': 'https://www.eyeem.com/u/{}',
    'Dribbble': 'https://dribbble.com/{}',
    'Members Fotki': 'https://members.fotki.com/{}/about',
    'Sound Cloud': 'https://soundcloud.com/{}',
    'Weibo': 'https://www.weibo.com/{}',
    'Kiwi Box': 'https://www.kiwibox.com/author/{}',
    'Forums Opera': 'https://forums.opera.com/user/{}',
    'Revista Forum': 'https://revistaforum.com.br/autor/{}.html',
    'Viex Americanas': 'https://www.viex-americas.com/{}',
    'Community Kobotoolbox': 'https://community.kobotoolbox.org/u/{}/summary',
    'Forum Asana': 'https://forum.asana.com/u/{}/summary',
    'UFBA Academia': 'https://ufba.academia.edu/{}',
    'Community': 'https://community.auth0.com/u/{}/summary',
    'Marautomation': 'https://www.marautomation.com/blog/author/{}',
    'Social Bund': 'https://social.bund.de/@{}',
    'CurseForge': 'https://www.curseforge.com/members/{}/projects',
    'Hatrick Sport': 'https://www.hatricksport.net/author/{}',
    'Pikabu': 'https://pikabu.ru/@{}',
    'Cambaddies': 'https://cambaddies.com/{}/profile',
    'Amateurav': 'https://amateurav.com/en/model/{}',
    'X cafe': 'https://xcafe.com/models/{}/',
    'X cams': 'https://www.xcams.cam/en/profile/{}/',
    'Bigtitstokyo': 'https://bigtitstokyo.com/model/{}',
    'X-TG tube': 'https://x-tg.tube/models/{}/',
    'Javiku': 'https://www.javiku.com/actor/{}/',
    'Watchjavpornonline author': 'https://watchjavpornonline.com/author/{}/',
    'Watchjavpornonline actor': 'https://watchjavpornonline.com/actor/{}/',
    'Proton VPN': 'https://protonvpn.com/blog/author/{}',
    'Nord VPN': 'https://nordvpn.com/pt-br/blog/author/{}/',
    'Crunchyroll': 'https://www.crunchyroll.com/pt-br/news/author/{}',
    'Pzwiki': 'https://pzwiki.wdka.nl/mediadesign/{}',
    'Eyewiki': 'https://eyewiki.org/User:{}',
    'DMOJ': 'https://dmoj.ca/user/{}',
    'Hebrew Books': 'https://qa.hebrewbooks.org/user/{}',
    'Spi jskaart': 'https://spijskaart.menu/user/{}',
    'Meettechniek': 'https://meettechniek.info/user/{}.html',
    'Purpose Games': 'https://www.purposegames.com/user/{}',
    'Bioengineering': 'https://bioengineering.gatech.edu/index.php/user/{}',
    'Enter Prisers Project': 'https://enterprisersproject.com/user/{}',
    'AMCS Community': 'https://amcs-community.org/user/{}/',
    'Lalp': 'https://lalp.melian.me/user/{}',
    'Godot': 'https://godot.community/user/{}',
    'XCP-user': 'https://xcp-ng.org/forum/user/{}',
    'XPC-groups': 'https://xcp-ng.org/forum/groups/{}',
    'Babel': 'https://www.babelcube.com/user/{}',
    'Booooooooom': 'https://www.booooooom.com/user/{}/',
    'Onlexpa': 'https://www.onlexpa.com/mk/user/{}',
    'Community Ipinfo': 'https://community.ipinfo.io/u/{}/summary',
    'Meme Droid': 'https://www.memedroid.com/user/view/{}',
    'Snack Video': 'https://www.snackvideo.com/@{}',
    'Uncams': 'https://uncams.com/{}',
    'Fansly': 'https://fansly.com/{}/posts',
    'Link Tr': 'https://linktr.ee/{}',
    'PWA': 'https://pwa.oohcams.com/details/{}',
    'Leaked Models': 'https://leakedmodels.org/{}/',
    'Archive Bate': 'http://archivebate.pro/profile/{}',
    'Nudes Puri': 'https://www.nudespuri.com/webcams/{}',
    'Infosec Exchange': 'https://infosec.exchange/@{}',
    'Spatial': 'https://www.spatial.io/@{}',
    'Open Sea': 'https://opensea.io/collection/{}',
    'Slideshare': 'https://pt.slideshare.net/{}',
    'Stories Strava': 'https://stories.strava.com/profiles/{}',
    'Patreon': 'https://www.patreon.com/{}',
    'Belling Cat': 'https://www.bellingcat.com/author/{}/',
    'CBT nuggets': 'https://www.cbtnuggets.com/{}',
    'Geeksforgeeks': 'https://www.geeksforgeeks.org/user/{}/',
    'Spice Works': 'https://www.spiceworks.com/user/about/{}',
    'Tomatazos': 'https://www.tomatazos.com/usuario/{}',
    'Epicdope': 'https://pt.epicdope.com/autor/{}/',
    'Ovicio': 'https://ovicio.com.br/author/{}/',
    'Animes Zone': 'https://animeszone.net/perfil/{}/',
    'Spirit Fanfiction': 'https://www.spiritfanfiction.com/perfil/{}',
    'Aniworld': 'https://aniworld.to/user/profil/{}',
    'Cinefy': 'https://cinefy.gg/{}',
    'Privacy': 'https://privacy.com.br/checkout/{}',
    'Live Pix': 'https://livepix.gg/{}',
    'Kick': 'https://kick.com/{}',
    'Flow Page': 'https://flow.page/{}',
    'Sex Log': 'https://pt-br.sexlog.com/u/{}',
    'Famosas Vip': 'https://famosas.vip/video/{}/',
    'The Pormap': 'https://thepornmap.com/pt/{}/',
    'Easeus': 'https://br.easeus.com/author/{}.html',
    'Vimeo': 'https://vimeo.com/{}',
    'Sciprofiles': 'https://sciprofiles.com/profile/{}',
    'Profiles UCLA': 'https://profiles.ucla.edu/{}',
    'Profiles SC CTSI': 'https://profiles.sc-ctsi.org/{}',
    'Crates': 'https://crates.io/users/{}',
    'Appsilon': 'https://www.appsilon.com/author/{}',
    'Researchgate': 'https://www.researchgate.net/profile/{}',
    'German Techjobs Companies': 'https://germantechjobs.de/companies/{}',
    'Stackoverflow': 'https://pt.stackoverflow.com/search?q={}',
    'Discuss AI Google.dev': 'https://discuss.ai.google.dev/u/{}/summary',
    'Meetup Community': 'https://www.meetup.com/{}/',
    'Meetup Blog': 'https://www.meetup.com/blog/author/{}/',
    'Wiki Benner': 'https://wiki.benner.com.br/accessviolation/?qa=user/{}',
    'Ask debxp': 'https://ask.debxp.org/user/{}',
    'Forum CSDMS': 'https://forum.csdms.io/u/{}/summary',
    'CSDMS Colorado': 'https://csdms.colorado.edu/wiki/User:{}',
    'Wiki Osgeo': 'https://wiki.osgeo.org/wiki/{}',
    'Wiki Osgeo User': 'https://wiki.osgeo.org/wiki/User:{}',
    'Wikimon': 'https://wikimon.net/User:{}',
    'Wiki Guildwars': 'https://wiki.guildwars.com/wiki/User:{}',
    'Docs Soften Sistemas': 'https://docs.softensistemas.com.br/user/{}',
    'Servicos2 Decea': 'https://servicos2.decea.mil.br/br-utm/wiki/user/{}',
    'Qa Hebrew Books': 'https://qa.hebrewbooks.org/user/{}',
    'Base IFPA': 'https://base.ifpa.edu.br/user/{}',
    'Manuais IFSP': 'https://manuais.ifsp.edu.br/user/{}',
    'Birdier': 'https://birdier.com/user/{}',
    'Habbo': 'https://www.habbo.com.br/profile/{}',
    'Soundversa AI': 'https://www.soundverse.ai/@{}', 
    'Tableau Blog': 'https://www.tableau.com/about/blog/contributors/{}',
    'Public Tableau': 'https://public.tableau.com/app/profile/{}/vizzes',
    'Publisko': 'https://publisko.com/profile/{}/groupings',
    'Idyllic': 'https://us.idyllic.app/profile/{}',
    'Divize Io': 'https://divize.io/profile/{}',
    'Vinte Conto': 'https://vinteconto.com.br/public/profile/{}',
    'KTH': 'https://www.kth.se/profile/{}',
    'Desigrush': 'https://www.designrush.com/agency/profile/{}',
    'Picuki': 'https://www.picuki.com/profile/{}',
    'Erlc': 'https://erlc.com/profile/{}/',
    'Talenta': 'https://www.e-talenta.eu/members/profile/{}',
    'The Meplaza': 'https://themeplaza.art/profile/{}',
    'Forums Kali': 'https://forums.kali.org/u/{}/summary',
    'Slideshare': 'https://www.slideshare.net/{}',
    'Framapiaf': 'https://framapiaf.org/@{}',
    'Fediscience': 'https://fediscience.org/@{}',
    '3hentai': 'https://3hentai.net/artists/{}',
        'Itsfoss': 'https://itsfoss.com/author/{}/',
    'Itsfoss Community': 'https://itsfoss.community/u/{}/summary',
    'Dev': 'https://dev.to/{}',
    'HQ porner': 'https://hqporner.com/actress/{}',
    'Beeg': 'https://beeg.com/{}',
    'Beeg Live Sex': 'https://beeglivesex.com/{}',
    'Porntrex': 'https://www.porntrex.com/models/{}/',
    'Porngo': 'https://www.porngo.com/models/{}/',
    'Motherless M': 'https://motherless.com/m/{}',
    'Motherless G': 'https://motherless.com/g/{}',
    'You Porn': 'https://www.youporn.com/pornstar/{}/',
    'Txxx': 'https://txxx.com/channel/{}/',
    'Porndoe': 'https://porndoe.com/pornstars-profile/{}',
    'Pornhat': 'https://www.pornhat.com/models/{}/',
    'Pornhat Sites': 'https://www.pornhat.com/sites/{}',
    'Ok xxx Sites': 'https://ok.xxx/sites/{}/',
    'Ok xxx Models': 'https://ok.xxx/models/{}/',
    'Animezone': 'https://animezone.com.br/author/{}/',
    'Pornhoarder': 'https://w5.pornhoarder.tv/user/{}/',
    'Porno Reino Estudios': 'https://www.pornoreino.com/estudio/{}',
    'Porno Reino Channel': 'https://www.pornoreino.com/channel/{}',
    'Poringa': 'http://www.poringa.net/{}',
    'Muyzorras': 'https://www.muyzorras.com/usuarios/{}',
    'Muyzorras Canales': 'https://www.muyzorras.com/canales/{}',
    'Porno Gratis Diario': 'https://www.pornogratisdiario.com/canal/{}/',
    'Porno Gratis Online': 'https://www.pornogratis.online/{}',
    'Cheemsporn': 'https://cheemsporn.com/videos/actor/{}',
    'Lovingsiren Actor': 'https://lovingsiren.com/actor/{}/',
    'Lovingsiren Author': 'https://lovingsiren.com/author/{}/',
    'Tnaflix': 'https://www.tnaflix.com/profile/{}',
    'A Outra Metade Mulheres': 'https://aoutrametade.com.br/Mulheres/{}',
    'A Outra Metade Homens': 'https://aoutrametade.com.br/Homens/{}',
    'Elenco Digital': 'https://elencodigital.com.br/{}',
    'Wordpress': 'https://{}.wordpress.com/',
    'Mixcloud': 'https://www.mixcloud.com/{}/',
    'Garoto Com Local': 'https://garotocomlocal.com.br/acompanhante-masculino/{}/',
    'Dailymotion': 'https://www.dailymotion.com/{}',
    'Garota Relax': 'https://garotarelax.com.br/df/acompanhantes/listing/{}/',
    'Letras': 'https://www.letras.com/{}/',
    'Webflow': 'https://webflow.com/@{}',
    'Rumble': 'https://rumble.com/user/{}',
    'Tecnoblog': 'https://tecnoblog.net/author/{}/',
    'Anime New': 'https://animenew.com.br/author/{}/',
    'Hackaday': 'https://hackaday.com/author/{}/',
    'Crackmes': 'https://crackmes.one/user/{}',
    'Wikipedia': 'https://pt.wikipedia.org/wiki/{}',
    'Clube da Rede': 'https://clubedarede.com/author/{}/',
    'Play Pilot': 'https://www.playpilot.com/br/user/{}/',
    'Cara app': 'https://cara.app/{}/all',
    'Ign': 'https://www.ign.com/person/{}',
    'Sharesome': 'https://sharesome.com/topic/{}/',
    'Holopin': 'https://www.holopin.io/@{}#',
    'Tellonym': 'https://tellonym.me/{}',
    'Fortnitetracker': 'https://fortnitetracker.com/profile/all/{}',
    'Forum Hack The box': 'https://forum.hackthebox.com/u/{}/summary',
    '9Gag Interest': 'https://9gag.com/interest/{}',
    'Pokemons Showdown': 'https://pokemonshowdown.com/users/{}',
    'Convite Discord': 'https://discord.com/invite/{}',
    'Lol Profile Champion': 'https://lolprofile.net/champion/{}',
    'Buymeacoffee': 'https://buymeacoffee.com/{}',
    'Steam Community ID': 'https://steamcommunity.com/id/{}',
    'Steam Community Groups': 'https://steamcommunity.com/groups/{}',
    'Bit Bucket': 'https://bitbucket.org/{}/',
    'Club House': 'https://www.clubhouse.com/@{}',
    'Bandcamp': 'https://bandcamp.com/{}',
    'Book Crossing': 'https://www.bookcrossing.com/mybookshelf/{}/',
    'Book Crossing Artists': 'https://www.bookcrossing.com/artists/{}',
    'Free Sound': 'https://freesound.org/people/{}/',
    'Pubg': 'https://pubg.op.gg/user/{}',
    'Blog Gravatar': 'https://blog.gravatar.com/author/{}/',
    'Skill Share': 'https://www.skillshare.com/pt/user/{}',
    'Forum Sublime Text': 'https://forum.sublimetext.com/u/{}/summary',
    'Community Signal Users': 'https://community.signalusers.org/u/{}/summary',
    'Unsplash': 'https://unsplash.com/@{}',
}
# Essa função é responsável por buscar o conteúdo de uma página web, fazendo uma requisição HTTP usando a biblioteca requests.
def get_page_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
        }
# Cabeçalhos (headers): O User-Agent é um cabeçalho HTTP que simula uma requisição feita por um navegador.        
        response = requests.get(url, headers=headers, timeout=9) # timeout=15 define que a requisição deve falhar se não for respondida em 15 segundos.
        if response.status_code == 200:# checa se o código de status HTTP retornado pela página é 200, que é "OK".
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e: # Captura exceções caso a requisição falhe (por exemplo, problemas de rede, servidor não encontrado, etc.)
        print(f'[!] Erro ao acessar {url}: {e}')
        return None

# Função para verificar se o nome de usuário está presente em alguma rede social
def check_social_media(username):
    results_found = False
    for social_media, url_template in social_media_urls.items(): # Esse dicionário contém as URLs base de diversas redes sociais.
        base_url = url_template.format(username) # Para cada rede social, o código substitui o {} na URL pelo nome de usuário fornecido, criando o link completo pro perfil.
        try:
            content = get_page_content(base_url) # Chama a função get_page_content para buscar o conteúdo da página de perfil da rede social.
            if content:
                soup = BeautifulSoup(content, 'html.parser')
# Usa a biblioteca BeautifulSoup pra parsear o HTML retornado. Essa biblioteca facilita a extração de informações do HTML de forma estruturada.
# Função soup.get_text() pega o texto visível da página HTML. A verificação if username in soup.get_text() checa se o nome de usuário está presente na página.
                if username in soup.get_text():
                    print(f'[+] Username encontrado no {social_media}: {base_url}')
                    results_found = True

        except Exception as e:
            print(f'[!] Erro de requisição para {social_media}: {e}')

        # Atraso de 1 segundo entre cada requisição
        time.sleep(1)  # Aguarda 1 segundo antes de fazer a próxima requisição.

    if not results_found:
        print(f'[-] Nenhum resultado encontrado para o username "{username}"')

# Função principal para iniciar a busca
def sherlock(username):
    print(f'[+] Iniciando busca por "{username}"...\n')
    check_social_media(username)

# Função para lidar com argumentos fornecidos ao script quando executado pela de linha de comando
def main():
    # Criando o parser de argumentos
    parser = argparse.ArgumentParser(description="Verifique se um usuário existe em diversas redes sociais.")
    parser.add_argument("username", help="Nome de usuário a ser verificado")

    # Parse do argumento
    args = parser.parse_args()

    # Chama a função de verificação com o nome de usuário fornecido
    sherlock(args.username)
# Esse trecho é uma verificação padrão para garantir que o código seja executado apenas quando o script for chamado    
if __name__ == "__main__":
    main()
