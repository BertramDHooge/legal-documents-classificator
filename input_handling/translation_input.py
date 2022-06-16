import os
import time
import pandas as pd
import googletrans
from googletrans import Translator

translator = Translator()
translator.raise_Exception = True

# the text may be too long, so we will break it into chunks

def get_chunks(s, maxlength, separator):
    start = 0
    end = 0
    while start + maxlength  < len(s) and end != -1:
        end = s.rfind(separator, start, start + maxlength + 1)
        yield s[start:end]
        start = end +1
    yield s[start:]

output = ""

def translate_text(text):
    text = text
    number_of_characters = len(text)
    global output
        
    if number_of_characters > 5000:
        
        for group in get_chunks(text, 5000, "."):
            if len(group) < 5000:
                group = translator.translate(group)
                output = output + group.text
            else:
                for group in get_chunks(text, 5000, ";"):
                    
                    if len(group) < 5000:
                        group = translator.translate(group)
                        output = output + group.text
                    else:
                        for group in get_chunks(text, 5000, ","):
                            if len(group) < 5000:
                                group = translator.translate(group)
                                output = output + group.text
                
            
    else:
        output = translator.translate(text)
        output = output.text
    return output


#string = "de Staat Malta tot het vermijden van dubbele belasting en tot het voorkomen van het ontgaan van belasting, en het Protocol, ondertekend te Brussel op 28 juni 1974, zoals gewijzigd door de Aanvullende Overeenkomst ondertekend te Brussel op 23 juni 1993 (1)(2)(3)FILIP, Koning der Belgen,Aan allen die nu zijn en hierna wezenzullen, Onze Groet.De Kamer van volksvertegenwoordigers heeft aangenomen en Wij bekrachtigen,hetgeen volgt :Artikel 1. Deze wet regelt een aangelegenheid als bedoeld in artikel 74 vande Grondwet.Art. 2. Het Protocol, gedaan te Brussel op 19 januari 2010, tot wijziging van deOvereenkomst tussen het Koninkrijk België en de Staat Malta tot het vermijden van dubbele belasting entot het voorkomen van het ontgaan van belasting, en het Protocol, ondertekend te Brussel op 28 juni 1974,zoals gewijzigd door de Aanvullende Overeenkomst ondertekend te Brussel op 23 juni 1993, zal volkomengevolg hebben.Kondigen deze wet af, bevelen dat zij met 's Lands zegel zal worden bekleed endoor het Belgisch Staatsblad zal worden bekendgemaakt.Gegeven te Brussel, 11 september 2015.FILIPVanKoningswege :De Minister van Buitenlandse Zaken en Europese zaken,D. REYNDERSDeMinister van Financiën,J. VAN OVERTVELDTMet 's Lands zegel gezegeld :DeMinister van Justitie,K. GEENS_______Nota's(1) Kamer van volksvertegenwoordigers(www.dekamer.be):Stukken:.nr 54-1144.Integraal verslag: 02/07/2015.(2)Zie Decreet van de Vlaamse Gemeenschap/ het Vlaamse Gewest van 07/06/2013 (Belgisch Staatsblad van 10/07/2013),Decreet van de Franse Gemeenschap van 25/06/2015 (Belgisch Staatsblad van 08/07/2015), Decreet van deDuitstalige Gemeenschap van 02/03/2015 (Belgisch Staatsblad van 27/03/2015), Decreet van het Waalse Gewestvan 12/03/2015 (Belgisch Staatsblad van 24/03/2015), Ordonnantie van het Brusselse Hoofdstedelijk Gewestvan 23/06/2017 (Belgisch Staatsblad van 06/07/2017).(3) Datum inwerkingtreding : 31/07/2017(art. II).Protocol tot wijziging van de Overeenkomst tussen het KoninkrijkBelgië en de Staat Malta tot het vermijden van dubbele belasting en tot het voorkomen van het ontgaanvan belasting, en het Protocol, ondertekend te Brussel op 28 juni 1974, zoals gewijzigd door de AanvullendeOvereenkomst ondertekend te Brussel op 23 juni 1993DE REGERING VAN HET KONINKRIJK BELGIEEnDEREGERING VAN MALTA,WENSENDE de Overeenkomst te wijzigen tussen het Koninkrijk België en deStaat Malta tot het vermijden van dubbele belasting en tot het voorkomen van het ontgaan van belasting,en het Protocol, ondertekend te Brussel op 28 juni 1974, zoals gewijzigd door de op 23 juni 1993 te Brusselondertekende Aanvullende Overeenkomst (hierna te noemen "de Overeenkomst"),ZIJN HET VOLGENDEOVEREENGEKOMEN :ARTIKEL IDe tekst van artikel 26 van de Overeenkomst wordt opgehevenen vervangen door de volgende tekst :"1. De bevoegde autoriteiten van de overeenkomstsluitendeStaten wisselen de inlichtingen uit die naar verwachting relevant zijn voor de uitvoering van de bepalingenvan deze Overeenkomst of voor de toepassing of de tenuitvoerlegging van de nationale wetgeving met betrekkingtot belastingen van elke soort en benaming die worden geheven door of ten behoeve van de overeenkomstsluitendeStaten, voor zover de belastingheffing waarin die nationale wetgeving voorziet niet in strijd is metde Overeenkomst. De uitwisseling van inlichtingen wordt niet beperkt door de artikelen 1 en 2.2.De door een overeenkomstsluitende Staat ingevolge paragraaf 1 verkregen inlichtingen worden op dezelfdewijze geheim gehouden als inlichtingen die onder de nationale wetgeving van die Staat zijn verkregenen worden alleen ter kennis gebracht van personen of autoriteiten (daaronder begrepen rechterlijke instantiesen administratieve lichamen) die betrokken zijn bij de vestiging of invordering van de in paragraaf 1bedoelde belastingen, bij de tenuitvoerlegging of vervolging ter zake van die belastingen, bij de beslissingin beroepszaken die betrekking hebben op die belastingen, of bij het toezicht daarop. Deze personen ofautoriteiten gebruiken die inlichtingen slechts voor die doeleinden. Zij mogen deze inlichtingen kenbaarmaken tijdens openbare rechtszittingen of in rechterlijke beslissingen. Niettegenstaande het voorafgaande,mogen de inlichtingen die door een overeenkomstsluitende Staat zijn ontvangen voor andere doeleindenworden gebruikt indien ze overeenkomstig de wetgeving van beide Staten voor die andere doeleinden mogenworden gebruikt en indien de bevoegde autoriteit van de Staat die de inlichtingen verstrekt, de toestemminggeeft voor dat gebruik.3. In geen geval mogen de bepalingen van de paragrafen 1 en 2 aldusworden uitgelegd dat zij een overeenkomstsluitende Staat de verplichting opleggen :(a) administratievemaatregelen te nemen die afwijken van de wetgeving en de administratieve praktijk van die of van de andereovereenkomstsluitende Staat;(b) inlichtingen te verstrekken die niet verkrijgbaar zijn volgensde wetgeving of in de normale gang van de administratieve werkzaamheden van die of van de andere overeenkomstsluitendeStaat;(c) inlichtingen te verstrekken die een handels-, bedrijfs-, nijverheids- of beroepsgeheimof een handelswerkwijze zouden onthullen, dan wel inlichtingen waarvan het verstrekken in strijd zouzijn met de openbare orde.4. Wanneer op basis van de bepalingen van dit artikel door een overeenkomstsluitendeStaat om inlichtingen is verzocht, gebruikt de andere overeenkomstsluitende Staat de middelen waaroverhij beschikt om de gevraagde inlichtingen te verkrijgen, zelfs al heeft die andere Staat die inlichtingenniet nodig voor zijn eigen belastingdoeleinden. De verplichting die in de vorige zin is vervat, is onderworpenaan de beperkingen waarin paragraaf 3 van dit artikel voorziet, maar die beperkingen mogen in geen gevalaldus worden uitgelegd dat ze een overeenkomstsluitende Staat toestaan het verstrekken van inlichtingente weigeren enkel omdat die Staat geen binnenlands belang heeft bij die inlichtingen.5. Ingeen geval mogen de bepalingen van paragraaf 3 van dit artikel aldus worden uitgelegd dat ze een overeenkomstsluitendeStaat toestaan om het verstrekken van inlichtingen te weigeren enkel en alleen omdat de inlichtingenin het bezit zijn van een bank, een andere financiële instelling, een trust, een stichting, een gevolmachtigdeof een persoon die werkzaam is in de hoedanigheid van een vertegenwoordiger of een vertrouwenspersoonof omdat de inlichtingen betrekking hebben op eigendomsbelangen in een persoon. Teneinde zulke inlichtingente verkrijgen heeft de belastingadministratie van de aangezochte overeenkomstsluitende Staat de bevoegdheidom te vragen inlichtingen kenbaar te maken en om een onderzoek en verhoren in te stellen, niettegenstaandeandersluidende bepalingen in de binnenlandse belastingwetgeving van die Staat."ARTIKEL IIElkvan de overeenkomstsluitende Staten stelt de andere overeenkomstsluitende Staat langs diplomatieke wegin kennis van de voltooiing van de procedures die door zijn wetgeving voor de inwerkingtreding van ditProtocol is vereist. Het Protocol zal in werking treden op de datum van de laatste van deze kennisgevingenen de bepalingen ervan zullen van toepassing zijn :a) met betrekking tot de bij de bron verschuldigdebelastingen op inkomsten die zijn toegekend of betaalbaar gesteld op of na 1 januari van het jaar datonmiddellijk volgt op het jaar waarin het Protocol in werking is getreden;b) met betrekkingtot de andere belastingen die worden geheven van inkomsten van belastbare tijdperken die aanvangen opof na 1 januari van het jaar dat onmiddellijk volgt op het jaar waarin het Protocol in werking is getreden;c)met betrekking tot alle andere belastingen geheven door of ten behoeve van de overeenkomstsluitende Staten,op elke andere belasting die verschuldigd is ter zake van belastbare feiten die zich voordoen op of na1 januari van het jaar dat onmiddellijk volgt op het jaar waarin het Protocol in werking is getreden.ARTIKELIIIDit Protocol, dat een integrerend deel van de Overeenkomst zal vormen, zal van kracht blijvenzolang de Overeenkomst van kracht blijft en zal van toepassing zijn zolang de Overeenkomst zelf van toepassingis.TEN BLIJKE WAARVAN de ondergetekenden, daartoe behoorlijk gevolmachtigd door hun respectieveRegeringen, dit Protocol hebben ondertekend.GEDAAN in tweevoud te Brussel, op 19 januari 2010,in de Engelse taal.PROTOCOL AMENDING THE AGREEMENT BETWEEN THE KINGDOM OF BELGIUMAND THE STATE OF MALTA FOR THE AVOIDANCE OF DOUBLE TAXATION AND THE PREVENTION OF FISCAL EVASION, ANDTHE PROTOCOL, SIGNED AT BRUSSELS ON 28 JUNE 1974 AS AMENDED BY THE SUPPLEMENTARY AGREEMENT SIGNED ATBRUSSELS ON 23 JUNE 1993THE GOVERNMENT OF THE KINGDOM OF BELGIUMANDTHEGOVERNMENT OF MALTA,DESIRING to amend the Agreement between the Kingdom of Belgium and theState of Malta for the avoidance of double taxation and the prevention of fiscal evasion, and the Protocol,signed at Brussels on 28 June 1974, as amended by the supplementary Agreement signed at Brussels on 23June 1993,(hereinafter referred to as "the Agreement"),HAVE AGREED as follows:ARTICLEIThe text of Article 26 of the Agreement is deleted and replaced by the following:1.The competent authorities of the Contracting States shall exchange such information as is foreseeablyrelevant for carrying out the provisions of this Agreement or to the administration or enforcement ofthe domestic laws concerning taxes of every kind and description imposed by or on behalf of the ContractingStates, insofar as the taxation thereunder is not contrary to the Agreement. The exchange of informationis not restricted by Articles 1 and 2.2. Any information received under paragraph 1 by a ContractingState shall be treated as secret in the same manner as information obtained under the domestic laws ofthat State and shall be disclosed only to persons or authorities (including courts and administrativebodies) concerned with the assessment or collection of, the enforcement or prosecution in respect of,the determination of appeals in relation to the taxes referred to in paragraph 1, or the oversight ofthe above. Such persons or authorities shall use the information only for such purposes. They may disclosethe information in public court proceedings or in judicial decisions. Notwithstanding the foregoing,information received by a Contracting State may be used for other purposes when such information maybe used for such other purposes under the laws of both States and the competent authority of the supplyingState authorises such use.3. In no case shall the provisions of paragraphs 1 and 2 be construedso as to impose on a Contracting State the obligation:(a) to carry out administrative measuresat variance with the laws and administrative practice of that or of the other Contracting State;(b)to supply information which is not obtainable under the laws or in the normal course of the administrationof that or of the other Contracting State;(c) to supply information which would disclose anytrade, business, industrial, commercial or professional secret or trade process, or information, thedisclosure of which would be contrary to public policy (ordre public).4. If information isrequested by a Contracting State in accordance with the provisions of this Article, the other ContractingState shall use its information gathering measures to obtain the requested information, even though thatother State may not need such information for its own tax purposes. The obligation contained in the precedingsentence is subject to the limitations of paragraph 3 of this Article but in no case shall such limitationsbe construed to permit a Contracting State to decline to supply information solely because it has nodomestic interest in such information.5. In no case shall the provisions of paragraph 3 ofthis Article be construed to permit a Contracting State to decline to supply information solely becausethe information is held by a bank, other financial institution, trust, foundation, nominee or personacting in an agency or a fiduciary capacity or because it relates to ownership interests in a person.In order to obtain such information the tax administration of the requested Contracting State shall havethe power to ask for the disclosure of information and to conduct investigations and hearings notwithstandingany contrary provisions in its domestic tax laws.ARTICLE IIEach of the ContractingStates shall notify the other Contracting State, through diplomatic channels, of the completion of theprocedures required by its law for the bringing into force of this Protocol. The Protocol shall enterinto force on the date of the later of these notifications and its provisions shall have effect:a)with respect to taxes due at source on income credited or payable on or after January 1 of the year nextfollowing the year in which the Protocol entered into force;b) with respect to other taxescharged on income of taxable periods beginning on or after January 1 of the year next following the yearin which the Protocol entered into force;c) with respect to any other taxes imposed by or onbehalf of the Contracting States, on any other tax due in respect of taxable events taking place on orafter January 1 of the year next following the year in which the Protocol entered into force.ARTICLEIIIThis Protocol, which shall form an integral part of the Agreement, shall remain in forceas long as the Agreement remains in force and shall apply as long as the Agreement itself is applicable.INWITNESS WHEREOF, the undersigned duly authorised thereto by their respective governments, have signedthis Protocol.DONE in duplicate at Brussels, on this 19th day of January 2010, in the Englishlanguage."
#translation = translate_doc(string)