# Pokémon TCG Deck Analysis

## Cluster Analysis


<script>
function filterTable() {
    const meanRankMin = parseFloat(document.getElementById('meanRankMin').value) || -Infinity;
    const meanRankMax = parseFloat(document.getElementById('meanRankMax').value) || Infinity;
    const deckCountMin = parseInt(document.getElementById('deckCountMin').value) || -Infinity;
    const deckCountMax = parseInt(document.getElementById('deckCountMax').value) || Infinity;
    const mainPokemonFilter = document.getElementById('mainPokemonFilter').value.toLowerCase();
    const secondaryPokemonFilter = document.getElementById('secondaryPokemonFilter').value.toLowerCase();

    const rows = document.querySelectorAll('#clusterTable tbody tr');
    rows.forEach(row => {
        const meanRank = parseFloat(row.dataset.meanRank);
        const deckCount = parseInt(row.dataset.deckCount);
        const mainPokemon = row.dataset.mainPokemon.toLowerCase();
        const secondaryPokemon = row.dataset.secondaryPokemon.toLowerCase();

        const matchesFilters =
            meanRank >= meanRankMin &&
            meanRank <= meanRankMax &&
            deckCount >= deckCountMin &&
            deckCount <= deckCountMax &&
            mainPokemon.includes(mainPokemonFilter) &&
            secondaryPokemon.includes(secondaryPokemonFilter);

        row.style.display = matchesFilters ? '' : 'none';
    });
}
</script>

<div>
    <label>Mean Rank Min: <input type="number" id="meanRankMin" oninput="filterTable()"></label>
    <label>Mean Rank Max: <input type="number" id="meanRankMax" oninput="filterTable()"></label>
    <label>Deck Count Min: <input type="number" id="deckCountMin" oninput="filterTable()"></label>
    <label>Deck Count Max: <input type="number" id="deckCountMax" oninput="filterTable()"></label>
    <label>Main Pokémon: <input type="text" id="mainPokemonFilter" oninput="filterTable()"></label>
    <label>Secondary Pokémon: <input type="text" id="secondaryPokemonFilter" oninput="filterTable()"></label>
</div>

<table id="clusterTable" border="1">
    <thead>
        <tr>
            <th>Cluster</th>
            <th>Mean Rank</th>
            <th>Main Pokémon</th>
            <th>Secondary Pokémon</th>
            <th>Deck Count</th>
            <th>Link</th>
        </tr>
    </thead>
    <tbody>

        <tr data-mean-rank="1.0" data-deck-count="1" data-main-pokemon="lugia" data-secondary-pokemon="archeops">
            <td>22</td>
            <td>1.00</td>
            <td>lugia</td>
            <td>archeops</td>
            <td>1</td>
            <td><a href="reports/cluster_22.md">Link</a></td>
        </tr>

        <tr data-mean-rank="1.0" data-deck-count="1" data-main-pokemon="alakazam" data-secondary-pokemon="xatu">
            <td>39</td>
            <td>1.00</td>
            <td>alakazam</td>
            <td>xatu</td>
            <td>1</td>
            <td><a href="reports/cluster_39.md">Link</a></td>
        </tr>

        <tr data-mean-rank="1.0" data-deck-count="1" data-main-pokemon="flareon" data-secondary-pokemon="noctowl">
            <td>265</td>
            <td>1.00</td>
            <td>flareon</td>
            <td>noctowl</td>
            <td>1</td>
            <td><a href="reports/cluster_265.md">Link</a></td>
        </tr>

        <tr data-mean-rank="2.0" data-deck-count="1" data-main-pokemon="pecharunt" data-secondary-pokemon="okidogi">
            <td>91</td>
            <td>2.00</td>
            <td>pecharunt</td>
            <td>okidogi</td>
            <td>1</td>
            <td><a href="reports/cluster_91.md">Link</a></td>
        </tr>

        <tr data-mean-rank="2.0" data-deck-count="1" data-main-pokemon="toedscruel" data-secondary-pokemon="ogerpon">
            <td>148</td>
            <td>2.00</td>
            <td>toedscruel</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_148.md">Link</a></td>
        </tr>

        <tr data-mean-rank="2.0" data-deck-count="1" data-main-pokemon="gardevoir" data-secondary-pokemon="munkidori">
            <td>236</td>
            <td>2.00</td>
            <td>gardevoir</td>
            <td>munkidori</td>
            <td>1</td>
            <td><a href="reports/cluster_236.md">Link</a></td>
        </tr>

        <tr data-mean-rank="2.0" data-deck-count="1" data-main-pokemon="raging-bolt" data-secondary-pokemon="ogerpon">
            <td>238</td>
            <td>2.00</td>
            <td>raging-bolt</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_238.md">Link</a></td>
        </tr>

        <tr data-mean-rank="2.0" data-deck-count="1" data-main-pokemon="toedscruel" data-secondary-pokemon="ogerpon">
            <td>368</td>
            <td>2.00</td>
            <td>toedscruel</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_368.md">Link</a></td>
        </tr>

        <tr data-mean-rank="2.0" data-deck-count="1" data-main-pokemon="hydrapple" data-secondary-pokemon="ogerpon">
            <td>437</td>
            <td>2.00</td>
            <td>hydrapple</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_437.md">Link</a></td>
        </tr>

        <tr data-mean-rank="2.5" data-deck-count="2" data-main-pokemon="roaring-moon" data-secondary-pokemon="flutter-mane">
            <td>152</td>
            <td>2.50</td>
            <td>roaring-moon</td>
            <td>flutter-mane</td>
            <td>2</td>
            <td><a href="reports/cluster_152.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="charizard">
            <td>57</td>
            <td>3.00</td>
            <td>noctowl</td>
            <td>charizard</td>
            <td>1</td>
            <td><a href="reports/cluster_57.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="typhlosion" data-secondary-pokemon="skeledirge">
            <td>72</td>
            <td>3.00</td>
            <td>typhlosion</td>
            <td>skeledirge</td>
            <td>1</td>
            <td><a href="reports/cluster_72.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="ceruledge" data-secondary-pokemon="None">
            <td>93</td>
            <td>3.00</td>
            <td>ceruledge</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_93.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="hydrapple" data-secondary-pokemon="thwackey">
            <td>146</td>
            <td>3.00</td>
            <td>hydrapple</td>
            <td>thwackey</td>
            <td>1</td>
            <td><a href="reports/cluster_146.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="tyranitar" data-secondary-pokemon="None">
            <td>160</td>
            <td>3.00</td>
            <td>tyranitar</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_160.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="yanmega" data-secondary-pokemon="dudunsparce">
            <td>167</td>
            <td>3.00</td>
            <td>yanmega</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_167.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="farigiraf" data-secondary-pokemon="milotic">
            <td>217</td>
            <td>3.00</td>
            <td>farigiraf</td>
            <td>milotic</td>
            <td>1</td>
            <td><a href="reports/cluster_217.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="armarouge" data-secondary-pokemon="ho-oh">
            <td>245</td>
            <td>3.00</td>
            <td>armarouge</td>
            <td>ho-oh</td>
            <td>1</td>
            <td><a href="reports/cluster_245.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="raging-bolt" data-secondary-pokemon="ogerpon">
            <td>276</td>
            <td>3.00</td>
            <td>raging-bolt</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_276.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>279</td>
            <td>3.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_279.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="2" data-main-pokemon="palafin" data-secondary-pokemon="pecharunt">
            <td>103</td>
            <td>3.00</td>
            <td>palafin</td>
            <td>pecharunt</td>
            <td>2</td>
            <td><a href="reports/cluster_103.md">Link</a></td>
        </tr>

        <tr data-mean-rank="3.0" data-deck-count="3" data-main-pokemon="crustle" data-secondary-pokemon="ogerpon-cornerstone">
            <td>306</td>
            <td>3.00</td>
            <td>crustle</td>
            <td>ogerpon-cornerstone</td>
            <td>3</td>
            <td><a href="reports/cluster_306.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>101</td>
            <td>4.00</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_101.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="dragapult" data-secondary-pokemon="None">
            <td>105</td>
            <td>4.00</td>
            <td>dragapult</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_105.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="crustle" data-secondary-pokemon="ogerpon-cornerstone">
            <td>112</td>
            <td>4.00</td>
            <td>crustle</td>
            <td>ogerpon-cornerstone</td>
            <td>1</td>
            <td><a href="reports/cluster_112.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="toedscruel" data-secondary-pokemon="ogerpon">
            <td>130</td>
            <td>4.00</td>
            <td>toedscruel</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_130.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="dipplin" data-secondary-pokemon="thwackey">
            <td>139</td>
            <td>4.00</td>
            <td>dipplin</td>
            <td>thwackey</td>
            <td>1</td>
            <td><a href="reports/cluster_139.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>159</td>
            <td>4.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_159.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="scovillain" data-secondary-pokemon="ogerpon">
            <td>169</td>
            <td>4.00</td>
            <td>scovillain</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_169.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>194</td>
            <td>4.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_194.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>195</td>
            <td>4.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_195.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>263</td>
            <td>4.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_263.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="raging-bolt" data-secondary-pokemon="ogerpon">
            <td>273</td>
            <td>4.00</td>
            <td>raging-bolt</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_273.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="conkeldurr" data-secondary-pokemon="pidgeot">
            <td>311</td>
            <td>4.00</td>
            <td>conkeldurr</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_311.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="blissey" data-secondary-pokemon="pecharunt">
            <td>412</td>
            <td>4.00</td>
            <td>blissey</td>
            <td>pecharunt</td>
            <td>1</td>
            <td><a href="reports/cluster_412.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.0" data-deck-count="1" data-main-pokemon="froslass" data-secondary-pokemon="espathra">
            <td>441</td>
            <td>4.00</td>
            <td>froslass</td>
            <td>espathra</td>
            <td>1</td>
            <td><a href="reports/cluster_441.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.5" data-deck-count="2" data-main-pokemon="metagross" data-secondary-pokemon="clefairy">
            <td>409</td>
            <td>4.50</td>
            <td>metagross</td>
            <td>clefairy</td>
            <td>2</td>
            <td><a href="reports/cluster_409.md">Link</a></td>
        </tr>

        <tr data-mean-rank="4.75" data-deck-count="4" data-main-pokemon="toedscruel" data-secondary-pokemon="ogerpon">
            <td>446</td>
            <td>4.75</td>
            <td>toedscruel</td>
            <td>ogerpon</td>
            <td>4</td>
            <td><a href="reports/cluster_446.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="flygon" data-secondary-pokemon="pidgeot">
            <td>37</td>
            <td>5.00</td>
            <td>flygon</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_37.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="metagross" data-secondary-pokemon="tatsugiri">
            <td>48</td>
            <td>5.00</td>
            <td>metagross</td>
            <td>tatsugiri</td>
            <td>1</td>
            <td><a href="reports/cluster_48.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="miraidon" data-secondary-pokemon="None">
            <td>99</td>
            <td>5.00</td>
            <td>miraidon</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_99.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="glaceon" data-secondary-pokemon="None">
            <td>187</td>
            <td>5.00</td>
            <td>glaceon</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_187.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="noctowl">
            <td>198</td>
            <td>5.00</td>
            <td>charizard</td>
            <td>noctowl</td>
            <td>1</td>
            <td><a href="reports/cluster_198.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="magneton">
            <td>200</td>
            <td>5.00</td>
            <td>noctowl</td>
            <td>magneton</td>
            <td>1</td>
            <td><a href="reports/cluster_200.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="iron-thorns" data-secondary-pokemon="None">
            <td>206</td>
            <td>5.00</td>
            <td>iron-thorns</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_206.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="aegislash" data-secondary-pokemon="dodrio">
            <td>250</td>
            <td>5.00</td>
            <td>aegislash</td>
            <td>dodrio</td>
            <td>1</td>
            <td><a href="reports/cluster_250.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>254</td>
            <td>5.00</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>1</td>
            <td><a href="reports/cluster_254.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="mimikyu" data-secondary-pokemon="ogerpon-cornerstone">
            <td>289</td>
            <td>5.00</td>
            <td>mimikyu</td>
            <td>ogerpon-cornerstone</td>
            <td>1</td>
            <td><a href="reports/cluster_289.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="palafin" data-secondary-pokemon="dudunsparce">
            <td>325</td>
            <td>5.00</td>
            <td>palafin</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_325.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="miraidon" data-secondary-pokemon="magneton">
            <td>326</td>
            <td>5.00</td>
            <td>miraidon</td>
            <td>magneton</td>
            <td>1</td>
            <td><a href="reports/cluster_326.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>411</td>
            <td>5.00</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_411.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.0" data-deck-count="2" data-main-pokemon="iron-valiant" data-secondary-pokemon="ogerpon">
            <td>285</td>
            <td>5.00</td>
            <td>iron-valiant</td>
            <td>ogerpon</td>
            <td>2</td>
            <td><a href="reports/cluster_285.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.333333333333333" data-deck-count="3" data-main-pokemon="grimmsnarl" data-secondary-pokemon="morpeko">
            <td>423</td>
            <td>5.33</td>
            <td>grimmsnarl</td>
            <td>morpeko</td>
            <td>3</td>
            <td><a href="reports/cluster_423.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.5" data-deck-count="2" data-main-pokemon="roaring-moon" data-secondary-pokemon="flutter-mane">
            <td>71</td>
            <td>5.50</td>
            <td>roaring-moon</td>
            <td>flutter-mane</td>
            <td>2</td>
            <td><a href="reports/cluster_71.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.5" data-deck-count="2" data-main-pokemon="aegislash" data-secondary-pokemon="tatsugiri">
            <td>156</td>
            <td>5.50</td>
            <td>aegislash</td>
            <td>tatsugiri</td>
            <td>2</td>
            <td><a href="reports/cluster_156.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.5" data-deck-count="2" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>316</td>
            <td>5.50</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>2</td>
            <td><a href="reports/cluster_316.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.571428571428571" data-deck-count="7" data-main-pokemon="zacian-crowned" data-secondary-pokemon="cramorant">
            <td>46</td>
            <td>5.57</td>
            <td>zacian-crowned</td>
            <td>cramorant</td>
            <td>7</td>
            <td><a href="reports/cluster_46.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.6" data-deck-count="10" data-main-pokemon="archaludon" data-secondary-pokemon="dudunsparce">
            <td>360</td>
            <td>5.60</td>
            <td>archaludon</td>
            <td>dudunsparce</td>
            <td>10</td>
            <td><a href="reports/cluster_360.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.625" data-deck-count="16" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>210</td>
            <td>5.62</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>16</td>
            <td><a href="reports/cluster_210.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.666666666666667" data-deck-count="3" data-main-pokemon="great-tusk" data-secondary-pokemon="great-tusk">
            <td>144</td>
            <td>5.67</td>
            <td>great-tusk</td>
            <td>great-tusk</td>
            <td>3</td>
            <td><a href="reports/cluster_144.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.666666666666667" data-deck-count="3" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>225</td>
            <td>5.67</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>3</td>
            <td><a href="reports/cluster_225.md">Link</a></td>
        </tr>

        <tr data-mean-rank="5.6923076923076925" data-deck-count="13" data-main-pokemon="ogerpon" data-secondary-pokemon="noctowl">
            <td>227</td>
            <td>5.69</td>
            <td>ogerpon</td>
            <td>noctowl</td>
            <td>13</td>
            <td><a href="reports/cluster_227.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="tinkaton" data-secondary-pokemon="dudunsparce">
            <td>47</td>
            <td>6.00</td>
            <td>tinkaton</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_47.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="garchomp">
            <td>52</td>
            <td>6.00</td>
            <td>mamoswine</td>
            <td>garchomp</td>
            <td>1</td>
            <td><a href="reports/cluster_52.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="dipplin" data-secondary-pokemon="None">
            <td>76</td>
            <td>6.00</td>
            <td>dipplin</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_76.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>104</td>
            <td>6.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_104.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="great-tusk" data-secondary-pokemon="None">
            <td>117</td>
            <td>6.00</td>
            <td>great-tusk</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_117.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="wugtrio" data-secondary-pokemon="ceruledge">
            <td>127</td>
            <td>6.00</td>
            <td>wugtrio</td>
            <td>ceruledge</td>
            <td>1</td>
            <td><a href="reports/cluster_127.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="dodrio" data-secondary-pokemon="ursaluna-bloodmoon">
            <td>168</td>
            <td>6.00</td>
            <td>dodrio</td>
            <td>ursaluna-bloodmoon</td>
            <td>1</td>
            <td><a href="reports/cluster_168.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="xatu" data-secondary-pokemon="slowking">
            <td>177</td>
            <td>6.00</td>
            <td>xatu</td>
            <td>slowking</td>
            <td>1</td>
            <td><a href="reports/cluster_177.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="dragapult" data-secondary-pokemon="lycanroc">
            <td>226</td>
            <td>6.00</td>
            <td>dragapult</td>
            <td>lycanroc</td>
            <td>1</td>
            <td><a href="reports/cluster_226.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="milotic" data-secondary-pokemon="ogerpon-cornerstone">
            <td>241</td>
            <td>6.00</td>
            <td>milotic</td>
            <td>ogerpon-cornerstone</td>
            <td>1</td>
            <td><a href="reports/cluster_241.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="1" data-main-pokemon="ceruledge" data-secondary-pokemon="squawkabilly">
            <td>341</td>
            <td>6.00</td>
            <td>ceruledge</td>
            <td>squawkabilly</td>
            <td>1</td>
            <td><a href="reports/cluster_341.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="2" data-main-pokemon="palafin" data-secondary-pokemon="dudunsparce">
            <td>34</td>
            <td>6.00</td>
            <td>palafin</td>
            <td>dudunsparce</td>
            <td>2</td>
            <td><a href="reports/cluster_34.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="2" data-main-pokemon="greninja" data-secondary-pokemon="pidgeot">
            <td>87</td>
            <td>6.00</td>
            <td>greninja</td>
            <td>pidgeot</td>
            <td>2</td>
            <td><a href="reports/cluster_87.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="2" data-main-pokemon="froslass" data-secondary-pokemon="espathra">
            <td>221</td>
            <td>6.00</td>
            <td>froslass</td>
            <td>espathra</td>
            <td>2</td>
            <td><a href="reports/cluster_221.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="2" data-main-pokemon="gholdengo" data-secondary-pokemon="scizor">
            <td>302</td>
            <td>6.00</td>
            <td>gholdengo</td>
            <td>scizor</td>
            <td>2</td>
            <td><a href="reports/cluster_302.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="2" data-main-pokemon="armarouge" data-secondary-pokemon="ho-oh">
            <td>402</td>
            <td>6.00</td>
            <td>armarouge</td>
            <td>ho-oh</td>
            <td>2</td>
            <td><a href="reports/cluster_402.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.0" data-deck-count="3" data-main-pokemon="dipplin" data-secondary-pokemon="thwackey">
            <td>312</td>
            <td>6.00</td>
            <td>dipplin</td>
            <td>thwackey</td>
            <td>3</td>
            <td><a href="reports/cluster_312.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.2" data-deck-count="5" data-main-pokemon="noivern" data-secondary-pokemon="squawkabilly">
            <td>128</td>
            <td>6.20</td>
            <td>noivern</td>
            <td>squawkabilly</td>
            <td>5</td>
            <td><a href="reports/cluster_128.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.333333333333333" data-deck-count="3" data-main-pokemon="mimikyu" data-secondary-pokemon="ogerpon-cornerstone">
            <td>126</td>
            <td>6.33</td>
            <td>mimikyu</td>
            <td>ogerpon-cornerstone</td>
            <td>3</td>
            <td><a href="reports/cluster_126.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.333333333333333" data-deck-count="3" data-main-pokemon="dudunsparce" data-secondary-pokemon="tyranitar">
            <td>432</td>
            <td>6.33</td>
            <td>dudunsparce</td>
            <td>tyranitar</td>
            <td>3</td>
            <td><a href="reports/cluster_432.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.428571428571429" data-deck-count="7" data-main-pokemon="noctowl" data-secondary-pokemon="azumarill">
            <td>235</td>
            <td>6.43</td>
            <td>noctowl</td>
            <td>azumarill</td>
            <td>7</td>
            <td><a href="reports/cluster_235.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.5" data-deck-count="2" data-main-pokemon="scovillain" data-secondary-pokemon="ogerpon">
            <td>143</td>
            <td>6.50</td>
            <td>scovillain</td>
            <td>ogerpon</td>
            <td>2</td>
            <td><a href="reports/cluster_143.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.5" data-deck-count="4" data-main-pokemon="espathra" data-secondary-pokemon="xatu">
            <td>208</td>
            <td>6.50</td>
            <td>espathra</td>
            <td>xatu</td>
            <td>4</td>
            <td><a href="reports/cluster_208.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.6" data-deck-count="5" data-main-pokemon="okidogi" data-secondary-pokemon="mimikyu">
            <td>434</td>
            <td>6.60</td>
            <td>okidogi</td>
            <td>mimikyu</td>
            <td>5</td>
            <td><a href="reports/cluster_434.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.6" data-deck-count="10" data-main-pokemon="aegislash" data-secondary-pokemon="squawkabilly">
            <td>55</td>
            <td>6.60</td>
            <td>aegislash</td>
            <td>squawkabilly</td>
            <td>10</td>
            <td><a href="reports/cluster_55.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.666666666666667" data-deck-count="3" data-main-pokemon="froslass" data-secondary-pokemon="milotic">
            <td>332</td>
            <td>6.67</td>
            <td>froslass</td>
            <td>milotic</td>
            <td>3</td>
            <td><a href="reports/cluster_332.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.666666666666667" data-deck-count="12" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>17</td>
            <td>6.67</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>12</td>
            <td><a href="reports/cluster_17.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.8" data-deck-count="5" data-main-pokemon="archaludon" data-secondary-pokemon="scizor">
            <td>344</td>
            <td>6.80</td>
            <td>archaludon</td>
            <td>scizor</td>
            <td>5</td>
            <td><a href="reports/cluster_344.md">Link</a></td>
        </tr>

        <tr data-mean-rank="6.8" data-deck-count="5" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>362</td>
            <td>6.80</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>5</td>
            <td><a href="reports/cluster_362.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="forretress" data-secondary-pokemon="noctowl">
            <td>95</td>
            <td>7.00</td>
            <td>forretress</td>
            <td>noctowl</td>
            <td>1</td>
            <td><a href="reports/cluster_95.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="archaludon" data-secondary-pokemon="dudunsparce">
            <td>106</td>
            <td>7.00</td>
            <td>archaludon</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_106.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="regidrago" data-secondary-pokemon="ogerpon">
            <td>113</td>
            <td>7.00</td>
            <td>regidrago</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_113.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="dragapult" data-secondary-pokemon="charizard">
            <td>136</td>
            <td>7.00</td>
            <td>dragapult</td>
            <td>charizard</td>
            <td>1</td>
            <td><a href="reports/cluster_136.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="magneton" data-secondary-pokemon="miraidon">
            <td>147</td>
            <td>7.00</td>
            <td>magneton</td>
            <td>miraidon</td>
            <td>1</td>
            <td><a href="reports/cluster_147.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="raging-bolt" data-secondary-pokemon="ho-oh">
            <td>185</td>
            <td>7.00</td>
            <td>raging-bolt</td>
            <td>ho-oh</td>
            <td>1</td>
            <td><a href="reports/cluster_185.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="mimikyu" data-secondary-pokemon="ogerpon-cornerstone">
            <td>284</td>
            <td>7.00</td>
            <td>mimikyu</td>
            <td>ogerpon-cornerstone</td>
            <td>1</td>
            <td><a href="reports/cluster_284.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>293</td>
            <td>7.00</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>1</td>
            <td><a href="reports/cluster_293.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="dudunsparce">
            <td>377</td>
            <td>7.00</td>
            <td>noctowl</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_377.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="1" data-main-pokemon="espathra" data-secondary-pokemon="ogerpon-cornerstone">
            <td>444</td>
            <td>7.00</td>
            <td>espathra</td>
            <td>ogerpon-cornerstone</td>
            <td>1</td>
            <td><a href="reports/cluster_444.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="2" data-main-pokemon="baxcalibur" data-secondary-pokemon="baxcalibur">
            <td>292</td>
            <td>7.00</td>
            <td>baxcalibur</td>
            <td>baxcalibur</td>
            <td>2</td>
            <td><a href="reports/cluster_292.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="2" data-main-pokemon="charizard" data-secondary-pokemon="cramorant">
            <td>304</td>
            <td>7.00</td>
            <td>charizard</td>
            <td>cramorant</td>
            <td>2</td>
            <td><a href="reports/cluster_304.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="2" data-main-pokemon="noctowl" data-secondary-pokemon="flareon">
            <td>400</td>
            <td>7.00</td>
            <td>noctowl</td>
            <td>flareon</td>
            <td>2</td>
            <td><a href="reports/cluster_400.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="2" data-main-pokemon="bellibolt" data-secondary-pokemon="kilowattrel">
            <td>416</td>
            <td>7.00</td>
            <td>bellibolt</td>
            <td>kilowattrel</td>
            <td>2</td>
            <td><a href="reports/cluster_416.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="3" data-main-pokemon="armarouge" data-secondary-pokemon="clefairy">
            <td>205</td>
            <td>7.00</td>
            <td>armarouge</td>
            <td>clefairy</td>
            <td>3</td>
            <td><a href="reports/cluster_205.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="3" data-main-pokemon="ogerpon" data-secondary-pokemon="armarouge">
            <td>259</td>
            <td>7.00</td>
            <td>ogerpon</td>
            <td>armarouge</td>
            <td>3</td>
            <td><a href="reports/cluster_259.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="3" data-main-pokemon="ogerpon" data-secondary-pokemon="brute-bonnet">
            <td>282</td>
            <td>7.00</td>
            <td>ogerpon</td>
            <td>brute-bonnet</td>
            <td>3</td>
            <td><a href="reports/cluster_282.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="6" data-main-pokemon="dragapult" data-secondary-pokemon="dudunsparce">
            <td>389</td>
            <td>7.00</td>
            <td>dragapult</td>
            <td>dudunsparce</td>
            <td>6</td>
            <td><a href="reports/cluster_389.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="14" data-main-pokemon="noctowl" data-secondary-pokemon="ogerpon">
            <td>361</td>
            <td>7.00</td>
            <td>noctowl</td>
            <td>ogerpon</td>
            <td>14</td>
            <td><a href="reports/cluster_361.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0" data-deck-count="16" data-main-pokemon="okidogi" data-secondary-pokemon="munkidori">
            <td>182</td>
            <td>7.00</td>
            <td>okidogi</td>
            <td>munkidori</td>
            <td>16</td>
            <td><a href="reports/cluster_182.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.0476190476190474" data-deck-count="21" data-main-pokemon="froslass" data-secondary-pokemon="espathra">
            <td>387</td>
            <td>7.05</td>
            <td>froslass</td>
            <td>espathra</td>
            <td>21</td>
            <td><a href="reports/cluster_387.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.055555555555555" data-deck-count="18" data-main-pokemon="milotic" data-secondary-pokemon="farigiraf">
            <td>384</td>
            <td>7.06</td>
            <td>milotic</td>
            <td>farigiraf</td>
            <td>18</td>
            <td><a href="reports/cluster_384.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.076923076923077" data-deck-count="13" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>415</td>
            <td>7.08</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>13</td>
            <td><a href="reports/cluster_415.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.1" data-deck-count="20" data-main-pokemon="blissey" data-secondary-pokemon="munkidori">
            <td>133</td>
            <td>7.10</td>
            <td>blissey</td>
            <td>munkidori</td>
            <td>20</td>
            <td><a href="reports/cluster_133.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.142857142857143" data-deck-count="7" data-main-pokemon="iron-valiant" data-secondary-pokemon="zacian-crowned">
            <td>219</td>
            <td>7.14</td>
            <td>iron-valiant</td>
            <td>zacian-crowned</td>
            <td>7</td>
            <td><a href="reports/cluster_219.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.142857142857143" data-deck-count="14" data-main-pokemon="typhlosion" data-secondary-pokemon="dudunsparce">
            <td>253</td>
            <td>7.14</td>
            <td>typhlosion</td>
            <td>dudunsparce</td>
            <td>14</td>
            <td><a href="reports/cluster_253.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.153846153846154" data-deck-count="13" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>61</td>
            <td>7.15</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>13</td>
            <td><a href="reports/cluster_61.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.208333333333333" data-deck-count="24" data-main-pokemon="flareon" data-secondary-pokemon="noctowl">
            <td>209</td>
            <td>7.21</td>
            <td>flareon</td>
            <td>noctowl</td>
            <td>24</td>
            <td><a href="reports/cluster_209.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.333333333333333" data-deck-count="3" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>134</td>
            <td>7.33</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>3</td>
            <td><a href="reports/cluster_134.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.333333333333333" data-deck-count="3" data-main-pokemon="dragapult" data-secondary-pokemon="charizard">
            <td>336</td>
            <td>7.33</td>
            <td>dragapult</td>
            <td>charizard</td>
            <td>3</td>
            <td><a href="reports/cluster_336.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.333333333333333" data-deck-count="12" data-main-pokemon="typhlosion" data-secondary-pokemon="dudunsparce">
            <td>375</td>
            <td>7.33</td>
            <td>typhlosion</td>
            <td>dudunsparce</td>
            <td>12</td>
            <td><a href="reports/cluster_375.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.4" data-deck-count="5" data-main-pokemon="galvantula" data-secondary-pokemon="miraidon">
            <td>138</td>
            <td>7.40</td>
            <td>galvantula</td>
            <td>miraidon</td>
            <td>5</td>
            <td><a href="reports/cluster_138.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.425" data-deck-count="40" data-main-pokemon="gardevoir" data-secondary-pokemon="munkidori">
            <td>20</td>
            <td>7.42</td>
            <td>gardevoir</td>
            <td>munkidori</td>
            <td>40</td>
            <td><a href="reports/cluster_20.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.454545454545454" data-deck-count="11" data-main-pokemon="archaludon" data-secondary-pokemon="revavroom">
            <td>281</td>
            <td>7.45</td>
            <td>archaludon</td>
            <td>revavroom</td>
            <td>11</td>
            <td><a href="reports/cluster_281.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.5" data-deck-count="2" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>74</td>
            <td>7.50</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>2</td>
            <td><a href="reports/cluster_74.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.5" data-deck-count="2" data-main-pokemon="azumarill" data-secondary-pokemon="noctowl">
            <td>243</td>
            <td>7.50</td>
            <td>azumarill</td>
            <td>noctowl</td>
            <td>2</td>
            <td><a href="reports/cluster_243.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.5" data-deck-count="2" data-main-pokemon="ceruledge" data-secondary-pokemon="pikachu">
            <td>430</td>
            <td>7.50</td>
            <td>ceruledge</td>
            <td>pikachu</td>
            <td>2</td>
            <td><a href="reports/cluster_430.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.5" data-deck-count="6" data-main-pokemon="mimikyu" data-secondary-pokemon="ogerpon-cornerstone">
            <td>140</td>
            <td>7.50</td>
            <td>mimikyu</td>
            <td>ogerpon-cornerstone</td>
            <td>6</td>
            <td><a href="reports/cluster_140.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.571428571428571" data-deck-count="7" data-main-pokemon="gholdengo" data-secondary-pokemon="dudunsparce">
            <td>291</td>
            <td>7.57</td>
            <td>gholdengo</td>
            <td>dudunsparce</td>
            <td>7</td>
            <td><a href="reports/cluster_291.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.588235294117647" data-deck-count="68" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>1</td>
            <td>7.59</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>68</td>
            <td><a href="reports/cluster_1.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.607843137254902" data-deck-count="102" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>11</td>
            <td>7.61</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>102</td>
            <td><a href="reports/cluster_11.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.608695652173913" data-deck-count="23" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>23</td>
            <td>7.61</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>23</td>
            <td><a href="reports/cluster_23.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.62962962962963" data-deck-count="27" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>395</td>
            <td>7.63</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>27</td>
            <td><a href="reports/cluster_395.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.653061224489796" data-deck-count="49" data-main-pokemon="typhlosion" data-secondary-pokemon="typhlosion">
            <td>239</td>
            <td>7.65</td>
            <td>typhlosion</td>
            <td>typhlosion</td>
            <td>49</td>
            <td><a href="reports/cluster_239.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.666666666666667" data-deck-count="3" data-main-pokemon="archaludon" data-secondary-pokemon="None">
            <td>49</td>
            <td>7.67</td>
            <td>archaludon</td>
            <td>None</td>
            <td>3</td>
            <td><a href="reports/cluster_49.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.666666666666667" data-deck-count="6" data-main-pokemon="dusknoir" data-secondary-pokemon="darmanitan">
            <td>443</td>
            <td>7.67</td>
            <td>dusknoir</td>
            <td>darmanitan</td>
            <td>6</td>
            <td><a href="reports/cluster_443.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.6875" data-deck-count="16" data-main-pokemon="raging-bolt" data-secondary-pokemon="ogerpon">
            <td>323</td>
            <td>7.69</td>
            <td>raging-bolt</td>
            <td>ogerpon</td>
            <td>16</td>
            <td><a href="reports/cluster_323.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.702127659574468" data-deck-count="94" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>390</td>
            <td>7.70</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>94</td>
            <td><a href="reports/cluster_390.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.714285714285714" data-deck-count="7" data-main-pokemon="archaludon" data-secondary-pokemon="zacian-crowned">
            <td>234</td>
            <td>7.71</td>
            <td>archaludon</td>
            <td>zacian-crowned</td>
            <td>7</td>
            <td><a href="reports/cluster_234.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.75" data-deck-count="20" data-main-pokemon="garchomp" data-secondary-pokemon="froslass">
            <td>67</td>
            <td>7.75</td>
            <td>garchomp</td>
            <td>froslass</td>
            <td>20</td>
            <td><a href="reports/cluster_67.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.75" data-deck-count="328" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>31</td>
            <td>7.75</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>328</td>
            <td><a href="reports/cluster_31.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.791666666666667" data-deck-count="48" data-main-pokemon="milotic" data-secondary-pokemon="farigiraf">
            <td>40</td>
            <td>7.79</td>
            <td>milotic</td>
            <td>farigiraf</td>
            <td>48</td>
            <td><a href="reports/cluster_40.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.8" data-deck-count="10" data-main-pokemon="yanmega" data-secondary-pokemon="dudunsparce">
            <td>410</td>
            <td>7.80</td>
            <td>yanmega</td>
            <td>dudunsparce</td>
            <td>10</td>
            <td><a href="reports/cluster_410.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.8133333333333335" data-deck-count="75" data-main-pokemon="noctowl" data-secondary-pokemon="charizard">
            <td>435</td>
            <td>7.81</td>
            <td>noctowl</td>
            <td>charizard</td>
            <td>75</td>
            <td><a href="reports/cluster_435.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.867924528301887" data-deck-count="53" data-main-pokemon="feraligatr" data-secondary-pokemon="munkidori">
            <td>6</td>
            <td>7.87</td>
            <td>feraligatr</td>
            <td>munkidori</td>
            <td>53</td>
            <td><a href="reports/cluster_6.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.901639344262295" data-deck-count="61" data-main-pokemon="dragapult" data-secondary-pokemon="iron-thorns">
            <td>262</td>
            <td>7.90</td>
            <td>dragapult</td>
            <td>iron-thorns</td>
            <td>61</td>
            <td><a href="reports/cluster_262.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.909090909090909" data-deck-count="11" data-main-pokemon="garchomp" data-secondary-pokemon="froslass">
            <td>381</td>
            <td>7.91</td>
            <td>garchomp</td>
            <td>froslass</td>
            <td>11</td>
            <td><a href="reports/cluster_381.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.913043478260869" data-deck-count="23" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>122</td>
            <td>7.91</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>23</td>
            <td><a href="reports/cluster_122.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.91358024691358" data-deck-count="81" data-main-pokemon="archaludon" data-secondary-pokemon="dudunsparce">
            <td>429</td>
            <td>7.91</td>
            <td>archaludon</td>
            <td>dudunsparce</td>
            <td>81</td>
            <td><a href="reports/cluster_429.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.947368421052632" data-deck-count="19" data-main-pokemon="ceruledge" data-secondary-pokemon="squawkabilly">
            <td>131</td>
            <td>7.95</td>
            <td>ceruledge</td>
            <td>squawkabilly</td>
            <td>19</td>
            <td><a href="reports/cluster_131.md">Link</a></td>
        </tr>

        <tr data-mean-rank="7.976190476190476" data-deck-count="84" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>314</td>
            <td>7.98</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>84</td>
            <td><a href="reports/cluster_314.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="dragapult" data-secondary-pokemon="None">
            <td>19</td>
            <td>8.00</td>
            <td>dragapult</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_19.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="magnezone" data-secondary-pokemon="miraidon">
            <td>97</td>
            <td>8.00</td>
            <td>magnezone</td>
            <td>miraidon</td>
            <td>1</td>
            <td><a href="reports/cluster_97.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="ogerpon">
            <td>183</td>
            <td>8.00</td>
            <td>noctowl</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_183.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>222</td>
            <td>8.00</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>1</td>
            <td><a href="reports/cluster_222.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>223</td>
            <td>8.00</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>1</td>
            <td><a href="reports/cluster_223.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="ceruledge" data-secondary-pokemon="None">
            <td>244</td>
            <td>8.00</td>
            <td>ceruledge</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_244.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="flareon" data-secondary-pokemon="jolteon">
            <td>303</td>
            <td>8.00</td>
            <td>flareon</td>
            <td>jolteon</td>
            <td>1</td>
            <td><a href="reports/cluster_303.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>315</td>
            <td>8.00</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>1</td>
            <td><a href="reports/cluster_315.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="1" data-main-pokemon="metagross" data-secondary-pokemon="dudunsparce">
            <td>436</td>
            <td>8.00</td>
            <td>metagross</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_436.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="2" data-main-pokemon="hydreigon" data-secondary-pokemon="pidgeot">
            <td>75</td>
            <td>8.00</td>
            <td>hydreigon</td>
            <td>pidgeot</td>
            <td>2</td>
            <td><a href="reports/cluster_75.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="2" data-main-pokemon="gardevoir" data-secondary-pokemon="munkidori">
            <td>96</td>
            <td>8.00</td>
            <td>gardevoir</td>
            <td>munkidori</td>
            <td>2</td>
            <td><a href="reports/cluster_96.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="2" data-main-pokemon="iron-crown" data-secondary-pokemon="iron-crown">
            <td>355</td>
            <td>8.00</td>
            <td>iron-crown</td>
            <td>iron-crown</td>
            <td>2</td>
            <td><a href="reports/cluster_355.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="2" data-main-pokemon="great-tusk" data-secondary-pokemon="squawkabilly">
            <td>392</td>
            <td>8.00</td>
            <td>great-tusk</td>
            <td>squawkabilly</td>
            <td>2</td>
            <td><a href="reports/cluster_392.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="2" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>397</td>
            <td>8.00</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>2</td>
            <td><a href="reports/cluster_397.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="4" data-main-pokemon="dipplin" data-secondary-pokemon="thwackey">
            <td>299</td>
            <td>8.00</td>
            <td>dipplin</td>
            <td>thwackey</td>
            <td>4</td>
            <td><a href="reports/cluster_299.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="7" data-main-pokemon="froslass" data-secondary-pokemon="munkidori">
            <td>329</td>
            <td>8.00</td>
            <td>froslass</td>
            <td>munkidori</td>
            <td>7</td>
            <td><a href="reports/cluster_329.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="9" data-main-pokemon="archaludon" data-secondary-pokemon="dudunsparce">
            <td>347</td>
            <td>8.00</td>
            <td>archaludon</td>
            <td>dudunsparce</td>
            <td>9</td>
            <td><a href="reports/cluster_347.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.0" data-deck-count="11" data-main-pokemon="milotic" data-secondary-pokemon="noivern">
            <td>29</td>
            <td>8.00</td>
            <td>milotic</td>
            <td>noivern</td>
            <td>11</td>
            <td><a href="reports/cluster_29.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.028301886792454" data-deck-count="212" data-main-pokemon="ogerpon" data-secondary-pokemon="noctowl">
            <td>56</td>
            <td>8.03</td>
            <td>ogerpon</td>
            <td>noctowl</td>
            <td>212</td>
            <td><a href="reports/cluster_56.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.041666666666666" data-deck-count="24" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>382</td>
            <td>8.04</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>24</td>
            <td><a href="reports/cluster_382.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.042168674698795" data-deck-count="166" data-main-pokemon="charizard" data-secondary-pokemon="noctowl">
            <td>5</td>
            <td>8.04</td>
            <td>charizard</td>
            <td>noctowl</td>
            <td>166</td>
            <td><a href="reports/cluster_5.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.046153846153846" data-deck-count="65" data-main-pokemon="gardevoir" data-secondary-pokemon="munkidori">
            <td>271</td>
            <td>8.05</td>
            <td>gardevoir</td>
            <td>munkidori</td>
            <td>65</td>
            <td><a href="reports/cluster_271.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.064814814814815" data-deck-count="324" data-main-pokemon="gardevoir" data-secondary-pokemon="munkidori">
            <td>32</td>
            <td>8.06</td>
            <td>gardevoir</td>
            <td>munkidori</td>
            <td>324</td>
            <td><a href="reports/cluster_32.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.071428571428571" data-deck-count="14" data-main-pokemon="hydrapple" data-secondary-pokemon="ogerpon">
            <td>174</td>
            <td>8.07</td>
            <td>hydrapple</td>
            <td>ogerpon</td>
            <td>14</td>
            <td><a href="reports/cluster_174.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.090909090909092" data-deck-count="33" data-main-pokemon="flareon" data-secondary-pokemon="noctowl">
            <td>351</td>
            <td>8.09</td>
            <td>flareon</td>
            <td>noctowl</td>
            <td>33</td>
            <td><a href="reports/cluster_351.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.105263157894736" data-deck-count="19" data-main-pokemon="garchomp" data-secondary-pokemon="roserade">
            <td>9</td>
            <td>8.11</td>
            <td>garchomp</td>
            <td>roserade</td>
            <td>19</td>
            <td><a href="reports/cluster_9.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.142857142857142" data-deck-count="28" data-main-pokemon="feraligatr" data-secondary-pokemon="munkidori">
            <td>407</td>
            <td>8.14</td>
            <td>feraligatr</td>
            <td>munkidori</td>
            <td>28</td>
            <td><a href="reports/cluster_407.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.152317880794701" data-deck-count="151" data-main-pokemon="archaludon" data-secondary-pokemon="squawkabilly">
            <td>356</td>
            <td>8.15</td>
            <td>archaludon</td>
            <td>squawkabilly</td>
            <td>151</td>
            <td><a href="reports/cluster_356.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.16256157635468" data-deck-count="406" data-main-pokemon="ogerpon" data-secondary-pokemon="ogerpon">
            <td>92</td>
            <td>8.16</td>
            <td>ogerpon</td>
            <td>ogerpon</td>
            <td>406</td>
            <td><a href="reports/cluster_92.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.1875" data-deck-count="128" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>428</td>
            <td>8.19</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>128</td>
            <td><a href="reports/cluster_428.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.2" data-deck-count="10" data-main-pokemon="flareon" data-secondary-pokemon="noctowl">
            <td>442</td>
            <td>8.20</td>
            <td>flareon</td>
            <td>noctowl</td>
            <td>10</td>
            <td><a href="reports/cluster_442.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.205673758865249" data-deck-count="141" data-main-pokemon="dragapult" data-secondary-pokemon="xatu">
            <td>137</td>
            <td>8.21</td>
            <td>dragapult</td>
            <td>xatu</td>
            <td>141</td>
            <td><a href="reports/cluster_137.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.21900826446281" data-deck-count="242" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>13</td>
            <td>8.22</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>242</td>
            <td><a href="reports/cluster_13.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.25" data-deck-count="4" data-main-pokemon="archaludon" data-secondary-pokemon="budew">
            <td>404</td>
            <td>8.25</td>
            <td>archaludon</td>
            <td>budew</td>
            <td>4</td>
            <td><a href="reports/cluster_404.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.25" data-deck-count="4" data-main-pokemon="archaludon" data-secondary-pokemon="revavroom">
            <td>439</td>
            <td>8.25</td>
            <td>archaludon</td>
            <td>revavroom</td>
            <td>4</td>
            <td><a href="reports/cluster_439.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.25" data-deck-count="8" data-main-pokemon="iron-crown" data-secondary-pokemon="iron-hands">
            <td>216</td>
            <td>8.25</td>
            <td>iron-crown</td>
            <td>iron-hands</td>
            <td>8</td>
            <td><a href="reports/cluster_216.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.266272189349113" data-deck-count="169" data-main-pokemon="gholdengo" data-secondary-pokemon="dudunsparce">
            <td>151</td>
            <td>8.27</td>
            <td>gholdengo</td>
            <td>dudunsparce</td>
            <td>169</td>
            <td><a href="reports/cluster_151.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.275" data-deck-count="40" data-main-pokemon="noctowl" data-secondary-pokemon="flareon">
            <td>193</td>
            <td>8.28</td>
            <td>noctowl</td>
            <td>flareon</td>
            <td>40</td>
            <td><a href="reports/cluster_193.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.285714285714286" data-deck-count="21" data-main-pokemon="froslass" data-secondary-pokemon="espathra">
            <td>38</td>
            <td>8.29</td>
            <td>froslass</td>
            <td>espathra</td>
            <td>21</td>
            <td><a href="reports/cluster_38.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.293103448275861" data-deck-count="58" data-main-pokemon="charizard" data-secondary-pokemon="dudunsparce">
            <td>129</td>
            <td>8.29</td>
            <td>charizard</td>
            <td>dudunsparce</td>
            <td>58</td>
            <td><a href="reports/cluster_129.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.31390134529148" data-deck-count="446" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>359</td>
            <td>8.31</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>446</td>
            <td><a href="reports/cluster_359.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.333333333333334" data-deck-count="15" data-main-pokemon="garchomp" data-secondary-pokemon="munkidori">
            <td>8</td>
            <td>8.33</td>
            <td>garchomp</td>
            <td>munkidori</td>
            <td>15</td>
            <td><a href="reports/cluster_8.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.35195530726257" data-deck-count="179" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>350</td>
            <td>8.35</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>179</td>
            <td><a href="reports/cluster_350.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.352941176470589" data-deck-count="34" data-main-pokemon="roaring-moon" data-secondary-pokemon="pecharunt">
            <td>257</td>
            <td>8.35</td>
            <td>roaring-moon</td>
            <td>pecharunt</td>
            <td>34</td>
            <td><a href="reports/cluster_257.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.432432432432432" data-deck-count="37" data-main-pokemon="zacian-crowned" data-secondary-pokemon="snorlax">
            <td>339</td>
            <td>8.43</td>
            <td>zacian-crowned</td>
            <td>snorlax</td>
            <td>37</td>
            <td><a href="reports/cluster_339.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.4375" data-deck-count="16" data-main-pokemon="ceruledge" data-secondary-pokemon="revavroom">
            <td>86</td>
            <td>8.44</td>
            <td>ceruledge</td>
            <td>revavroom</td>
            <td>16</td>
            <td><a href="reports/cluster_86.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.438223938223938" data-deck-count="518" data-main-pokemon="noctowl" data-secondary-pokemon="ogerpon">
            <td>0</td>
            <td>8.44</td>
            <td>noctowl</td>
            <td>ogerpon</td>
            <td>518</td>
            <td><a href="reports/cluster_0.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.444444444444445" data-deck-count="9" data-main-pokemon="aegislash" data-secondary-pokemon="tatsugiri">
            <td>278</td>
            <td>8.44</td>
            <td>aegislash</td>
            <td>tatsugiri</td>
            <td>9</td>
            <td><a href="reports/cluster_278.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.466666666666667" data-deck-count="30" data-main-pokemon="froslass" data-secondary-pokemon="munkidori">
            <td>313</td>
            <td>8.47</td>
            <td>froslass</td>
            <td>munkidori</td>
            <td>30</td>
            <td><a href="reports/cluster_313.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.46875" data-deck-count="32" data-main-pokemon="gholdengo" data-secondary-pokemon="dudunsparce">
            <td>164</td>
            <td>8.47</td>
            <td>gholdengo</td>
            <td>dudunsparce</td>
            <td>32</td>
            <td><a href="reports/cluster_164.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.476190476190476" data-deck-count="21" data-main-pokemon="ceruledge" data-secondary-pokemon="revavroom">
            <td>431</td>
            <td>8.48</td>
            <td>ceruledge</td>
            <td>revavroom</td>
            <td>21</td>
            <td><a href="reports/cluster_431.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.477611940298507" data-deck-count="67" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>15</td>
            <td>8.48</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>67</td>
            <td><a href="reports/cluster_15.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.478260869565217" data-deck-count="23" data-main-pokemon="bellibolt" data-secondary-pokemon="kilowattrel">
            <td>16</td>
            <td>8.48</td>
            <td>bellibolt</td>
            <td>kilowattrel</td>
            <td>23</td>
            <td><a href="reports/cluster_16.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.5" data-deck-count="2" data-main-pokemon="gholdengo" data-secondary-pokemon="dragapult">
            <td>275</td>
            <td>8.50</td>
            <td>gholdengo</td>
            <td>dragapult</td>
            <td>2</td>
            <td><a href="reports/cluster_275.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.5" data-deck-count="2" data-main-pokemon="archaludon" data-secondary-pokemon="dudunsparce">
            <td>331</td>
            <td>8.50</td>
            <td>archaludon</td>
            <td>dudunsparce</td>
            <td>2</td>
            <td><a href="reports/cluster_331.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.5" data-deck-count="2" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>345</td>
            <td>8.50</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>2</td>
            <td><a href="reports/cluster_345.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.524" data-deck-count="250" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>178</td>
            <td>8.52</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>250</td>
            <td><a href="reports/cluster_178.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.538461538461538" data-deck-count="13" data-main-pokemon="ceruledge" data-secondary-pokemon="drilbur">
            <td>294</td>
            <td>8.54</td>
            <td>ceruledge</td>
            <td>drilbur</td>
            <td>13</td>
            <td><a href="reports/cluster_294.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.615384615384615" data-deck-count="13" data-main-pokemon="mimikyu" data-secondary-pokemon="ogerpon-cornerstone">
            <td>417</td>
            <td>8.62</td>
            <td>mimikyu</td>
            <td>ogerpon-cornerstone</td>
            <td>13</td>
            <td><a href="reports/cluster_417.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.620689655172415" data-deck-count="29" data-main-pokemon="feraligatr" data-secondary-pokemon="milotic">
            <td>371</td>
            <td>8.62</td>
            <td>feraligatr</td>
            <td>milotic</td>
            <td>29</td>
            <td><a href="reports/cluster_371.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.666666666666666" data-deck-count="3" data-main-pokemon="banette" data-secondary-pokemon="banette">
            <td>114</td>
            <td>8.67</td>
            <td>banette</td>
            <td>banette</td>
            <td>3</td>
            <td><a href="reports/cluster_114.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.666666666666666" data-deck-count="3" data-main-pokemon="jolteon" data-secondary-pokemon="flareon">
            <td>419</td>
            <td>8.67</td>
            <td>jolteon</td>
            <td>flareon</td>
            <td>3</td>
            <td><a href="reports/cluster_419.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.666666666666666" data-deck-count="6" data-main-pokemon="dipplin" data-secondary-pokemon="dipplin">
            <td>27</td>
            <td>8.67</td>
            <td>dipplin</td>
            <td>dipplin</td>
            <td>6</td>
            <td><a href="reports/cluster_27.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.666666666666666" data-deck-count="36" data-main-pokemon="noctowl" data-secondary-pokemon="terapagos">
            <td>202</td>
            <td>8.67</td>
            <td>noctowl</td>
            <td>terapagos</td>
            <td>36</td>
            <td><a href="reports/cluster_202.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.68" data-deck-count="50" data-main-pokemon="ceruledge" data-secondary-pokemon="noctowl">
            <td>338</td>
            <td>8.68</td>
            <td>ceruledge</td>
            <td>noctowl</td>
            <td>50</td>
            <td><a href="reports/cluster_338.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.74074074074074" data-deck-count="27" data-main-pokemon="gholdengo" data-secondary-pokemon="dragapult">
            <td>2</td>
            <td>8.74</td>
            <td>gholdengo</td>
            <td>dragapult</td>
            <td>27</td>
            <td><a href="reports/cluster_2.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.75" data-deck-count="4" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>260</td>
            <td>8.75</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>4</td>
            <td><a href="reports/cluster_260.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.755555555555556" data-deck-count="45" data-main-pokemon="flareon" data-secondary-pokemon="sylveon">
            <td>62</td>
            <td>8.76</td>
            <td>flareon</td>
            <td>sylveon</td>
            <td>45</td>
            <td><a href="reports/cluster_62.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.777777777777779" data-deck-count="81" data-main-pokemon="archaludon" data-secondary-pokemon="scizor">
            <td>98</td>
            <td>8.78</td>
            <td>archaludon</td>
            <td>scizor</td>
            <td>81</td>
            <td><a href="reports/cluster_98.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.777777777777779" data-deck-count="135" data-main-pokemon="dragapult" data-secondary-pokemon="charizard">
            <td>84</td>
            <td>8.78</td>
            <td>dragapult</td>
            <td>charizard</td>
            <td>135</td>
            <td><a href="reports/cluster_84.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.795918367346939" data-deck-count="49" data-main-pokemon="iron-crown" data-secondary-pokemon="iron-hands">
            <td>25</td>
            <td>8.80</td>
            <td>iron-crown</td>
            <td>iron-hands</td>
            <td>49</td>
            <td><a href="reports/cluster_25.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.8" data-deck-count="5" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>327</td>
            <td>8.80</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>5</td>
            <td><a href="reports/cluster_327.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.818181818181818" data-deck-count="11" data-main-pokemon="dragapult" data-secondary-pokemon="blaziken">
            <td>445</td>
            <td>8.82</td>
            <td>dragapult</td>
            <td>blaziken</td>
            <td>11</td>
            <td><a href="reports/cluster_445.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.828729281767956" data-deck-count="181" data-main-pokemon="gholdengo" data-secondary-pokemon="dragapult">
            <td>58</td>
            <td>8.83</td>
            <td>gholdengo</td>
            <td>dragapult</td>
            <td>181</td>
            <td><a href="reports/cluster_58.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.875" data-deck-count="40" data-main-pokemon="raging-bolt" data-secondary-pokemon="ogerpon">
            <td>352</td>
            <td>8.88</td>
            <td>raging-bolt</td>
            <td>ogerpon</td>
            <td>40</td>
            <td><a href="reports/cluster_352.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.882352941176471" data-deck-count="17" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>320</td>
            <td>8.88</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>17</td>
            <td><a href="reports/cluster_320.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.909090909090908" data-deck-count="11" data-main-pokemon="archaludon" data-secondary-pokemon="scizor">
            <td>403</td>
            <td>8.91</td>
            <td>archaludon</td>
            <td>scizor</td>
            <td>11</td>
            <td><a href="reports/cluster_403.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.925925925925926" data-deck-count="27" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>190</td>
            <td>8.93</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>27</td>
            <td><a href="reports/cluster_190.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.933333333333334" data-deck-count="90" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>73</td>
            <td>8.93</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>90</td>
            <td><a href="reports/cluster_73.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.9375" data-deck-count="128" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>231</td>
            <td>8.94</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>128</td>
            <td><a href="reports/cluster_231.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.973451327433628" data-deck-count="113" data-main-pokemon="gholdengo" data-secondary-pokemon="scizor">
            <td>283</td>
            <td>8.97</td>
            <td>gholdengo</td>
            <td>scizor</td>
            <td>113</td>
            <td><a href="reports/cluster_283.md">Link</a></td>
        </tr>

        <tr data-mean-rank="8.994444444444444" data-deck-count="180" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>154</td>
            <td>8.99</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>180</td>
            <td><a href="reports/cluster_154.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="quaquaval">
            <td>4</td>
            <td>9.00</td>
            <td>mamoswine</td>
            <td>quaquaval</td>
            <td>1</td>
            <td><a href="reports/cluster_4.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="comfey" data-secondary-pokemon="None">
            <td>21</td>
            <td>9.00</td>
            <td>comfey</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_21.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="chandelure" data-secondary-pokemon="totodile">
            <td>54</td>
            <td>9.00</td>
            <td>chandelure</td>
            <td>totodile</td>
            <td>1</td>
            <td><a href="reports/cluster_54.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="hydreigon" data-secondary-pokemon="pidgeot">
            <td>109</td>
            <td>9.00</td>
            <td>hydreigon</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_109.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="tyranitar" data-secondary-pokemon="pidgeot">
            <td>120</td>
            <td>9.00</td>
            <td>tyranitar</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_120.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>150</td>
            <td>9.00</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_150.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="garchomp" data-secondary-pokemon="toedscruel">
            <td>153</td>
            <td>9.00</td>
            <td>garchomp</td>
            <td>toedscruel</td>
            <td>1</td>
            <td><a href="reports/cluster_153.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="ceruledge" data-secondary-pokemon="squawkabilly">
            <td>176</td>
            <td>9.00</td>
            <td>ceruledge</td>
            <td>squawkabilly</td>
            <td>1</td>
            <td><a href="reports/cluster_176.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="iron-crown" data-secondary-pokemon="iron-hands">
            <td>251</td>
            <td>9.00</td>
            <td>iron-crown</td>
            <td>iron-hands</td>
            <td>1</td>
            <td><a href="reports/cluster_251.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="ho-oh" data-secondary-pokemon="armarouge">
            <td>261</td>
            <td>9.00</td>
            <td>ho-oh</td>
            <td>armarouge</td>
            <td>1</td>
            <td><a href="reports/cluster_261.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="ogerpon" data-secondary-pokemon="noctowl">
            <td>287</td>
            <td>9.00</td>
            <td>ogerpon</td>
            <td>noctowl</td>
            <td>1</td>
            <td><a href="reports/cluster_287.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>335</td>
            <td>9.00</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>1</td>
            <td><a href="reports/cluster_335.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>353</td>
            <td>9.00</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>1</td>
            <td><a href="reports/cluster_353.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="1" data-main-pokemon="thwackey" data-secondary-pokemon="seaking">
            <td>386</td>
            <td>9.00</td>
            <td>thwackey</td>
            <td>seaking</td>
            <td>1</td>
            <td><a href="reports/cluster_386.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="2" data-main-pokemon="dipplin" data-secondary-pokemon="dipplin">
            <td>396</td>
            <td>9.00</td>
            <td>dipplin</td>
            <td>dipplin</td>
            <td>2</td>
            <td><a href="reports/cluster_396.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="3" data-main-pokemon="charizard" data-secondary-pokemon="charizard">
            <td>340</td>
            <td>9.00</td>
            <td>charizard</td>
            <td>charizard</td>
            <td>3</td>
            <td><a href="reports/cluster_340.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="6" data-main-pokemon="froslass" data-secondary-pokemon="lycanroc">
            <td>121</td>
            <td>9.00</td>
            <td>froslass</td>
            <td>lycanroc</td>
            <td>6</td>
            <td><a href="reports/cluster_121.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="7" data-main-pokemon="metang" data-secondary-pokemon="zacian">
            <td>125</td>
            <td>9.00</td>
            <td>metang</td>
            <td>zacian</td>
            <td>7</td>
            <td><a href="reports/cluster_125.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="9" data-main-pokemon="gouging-fire" data-secondary-pokemon="pecharunt">
            <td>277</td>
            <td>9.00</td>
            <td>gouging-fire</td>
            <td>pecharunt</td>
            <td>9</td>
            <td><a href="reports/cluster_277.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="12" data-main-pokemon="dragapult" data-secondary-pokemon="xatu">
            <td>295</td>
            <td>9.00</td>
            <td>dragapult</td>
            <td>xatu</td>
            <td>12</td>
            <td><a href="reports/cluster_295.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="20" data-main-pokemon="gholdengo" data-secondary-pokemon="dudunsparce">
            <td>301</td>
            <td>9.00</td>
            <td>gholdengo</td>
            <td>dudunsparce</td>
            <td>20</td>
            <td><a href="reports/cluster_301.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="21" data-main-pokemon="hydreigon" data-secondary-pokemon="pidgeot">
            <td>378</td>
            <td>9.00</td>
            <td>hydreigon</td>
            <td>pidgeot</td>
            <td>21</td>
            <td><a href="reports/cluster_378.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.0" data-deck-count="22" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>171</td>
            <td>9.00</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>22</td>
            <td><a href="reports/cluster_171.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.051282051282051" data-deck-count="156" data-main-pokemon="archaludon" data-secondary-pokemon="zacian-crowned">
            <td>12</td>
            <td>9.05</td>
            <td>archaludon</td>
            <td>zacian-crowned</td>
            <td>156</td>
            <td><a href="reports/cluster_12.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.095238095238095" data-deck-count="21" data-main-pokemon="flareon" data-secondary-pokemon="noctowl">
            <td>201</td>
            <td>9.10</td>
            <td>flareon</td>
            <td>noctowl</td>
            <td>21</td>
            <td><a href="reports/cluster_201.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.096774193548388" data-deck-count="31" data-main-pokemon="gardevoir" data-secondary-pokemon="scream-tail">
            <td>300</td>
            <td>9.10</td>
            <td>gardevoir</td>
            <td>scream-tail</td>
            <td>31</td>
            <td><a href="reports/cluster_300.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.1" data-deck-count="10" data-main-pokemon="blissey" data-secondary-pokemon="ogerpon">
            <td>166</td>
            <td>9.10</td>
            <td>blissey</td>
            <td>ogerpon</td>
            <td>10</td>
            <td><a href="reports/cluster_166.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.1" data-deck-count="40" data-main-pokemon="flareon" data-secondary-pokemon="sylveon">
            <td>358</td>
            <td>9.10</td>
            <td>flareon</td>
            <td>sylveon</td>
            <td>40</td>
            <td><a href="reports/cluster_358.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.142857142857142" data-deck-count="7" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>280</td>
            <td>9.14</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>7</td>
            <td><a href="reports/cluster_280.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.166666666666666" data-deck-count="6" data-main-pokemon="dodrio" data-secondary-pokemon="dodrio">
            <td>141</td>
            <td>9.17</td>
            <td>dodrio</td>
            <td>dodrio</td>
            <td>6</td>
            <td><a href="reports/cluster_141.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.170454545454545" data-deck-count="88" data-main-pokemon="noctowl" data-secondary-pokemon="charizard">
            <td>385</td>
            <td>9.17</td>
            <td>noctowl</td>
            <td>charizard</td>
            <td>88</td>
            <td><a href="reports/cluster_385.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.23076923076923" data-deck-count="13" data-main-pokemon="conkeldurr" data-secondary-pokemon="pidgeot">
            <td>53</td>
            <td>9.23</td>
            <td>conkeldurr</td>
            <td>pidgeot</td>
            <td>13</td>
            <td><a href="reports/cluster_53.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.25" data-deck-count="4" data-main-pokemon="iron-thorns" data-secondary-pokemon="None">
            <td>364</td>
            <td>9.25</td>
            <td>iron-thorns</td>
            <td>None</td>
            <td>4</td>
            <td><a href="reports/cluster_364.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.25" data-deck-count="4" data-main-pokemon="magcargo" data-secondary-pokemon="ho-oh">
            <td>369</td>
            <td>9.25</td>
            <td>magcargo</td>
            <td>ho-oh</td>
            <td>4</td>
            <td><a href="reports/cluster_369.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.25" data-deck-count="24" data-main-pokemon="crustle" data-secondary-pokemon="munkidori">
            <td>310</td>
            <td>9.25</td>
            <td>crustle</td>
            <td>munkidori</td>
            <td>24</td>
            <td><a href="reports/cluster_310.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.333333333333334" data-deck-count="6" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>354</td>
            <td>9.33</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>6</td>
            <td><a href="reports/cluster_354.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.333333333333334" data-deck-count="12" data-main-pokemon="garchomp" data-secondary-pokemon="froslass">
            <td>421</td>
            <td>9.33</td>
            <td>garchomp</td>
            <td>froslass</td>
            <td>12</td>
            <td><a href="reports/cluster_421.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.344827586206897" data-deck-count="29" data-main-pokemon="garchomp" data-secondary-pokemon="roserade">
            <td>398</td>
            <td>9.34</td>
            <td>garchomp</td>
            <td>roserade</td>
            <td>29</td>
            <td><a href="reports/cluster_398.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.379310344827585" data-deck-count="29" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>3</td>
            <td>9.38</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>29</td>
            <td><a href="reports/cluster_3.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.384615384615385" data-deck-count="78" data-main-pokemon="gholdengo" data-secondary-pokemon="typhlosion">
            <td>65</td>
            <td>9.38</td>
            <td>gholdengo</td>
            <td>typhlosion</td>
            <td>78</td>
            <td><a href="reports/cluster_65.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.473684210526315" data-deck-count="19" data-main-pokemon="hydreigon" data-secondary-pokemon="pidgeot">
            <td>180</td>
            <td>9.47</td>
            <td>hydreigon</td>
            <td>pidgeot</td>
            <td>19</td>
            <td><a href="reports/cluster_180.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.5" data-deck-count="2" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>123</td>
            <td>9.50</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>2</td>
            <td><a href="reports/cluster_123.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.5" data-deck-count="2" data-main-pokemon="froslass" data-secondary-pokemon="munkidori">
            <td>372</td>
            <td>9.50</td>
            <td>froslass</td>
            <td>munkidori</td>
            <td>2</td>
            <td><a href="reports/cluster_372.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.5" data-deck-count="6" data-main-pokemon="miraidon" data-secondary-pokemon="pikachu">
            <td>18</td>
            <td>9.50</td>
            <td>miraidon</td>
            <td>pikachu</td>
            <td>6</td>
            <td><a href="reports/cluster_18.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.5" data-deck-count="10" data-main-pokemon="grimmsnarl" data-secondary-pokemon="morpeko">
            <td>41</td>
            <td>9.50</td>
            <td>grimmsnarl</td>
            <td>morpeko</td>
            <td>10</td>
            <td><a href="reports/cluster_41.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.571428571428571" data-deck-count="14" data-main-pokemon="gholdengo" data-secondary-pokemon="togekiss">
            <td>94</td>
            <td>9.57</td>
            <td>gholdengo</td>
            <td>togekiss</td>
            <td>14</td>
            <td><a href="reports/cluster_94.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.6" data-deck-count="5" data-main-pokemon="archaludon" data-secondary-pokemon="dudunsparce">
            <td>422</td>
            <td>9.60</td>
            <td>archaludon</td>
            <td>dudunsparce</td>
            <td>5</td>
            <td><a href="reports/cluster_422.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.6" data-deck-count="5" data-main-pokemon="armarouge" data-secondary-pokemon="ho-oh">
            <td>426</td>
            <td>9.60</td>
            <td>armarouge</td>
            <td>ho-oh</td>
            <td>5</td>
            <td><a href="reports/cluster_426.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.6" data-deck-count="10" data-main-pokemon="archaludon" data-secondary-pokemon="dudunsparce">
            <td>399</td>
            <td>9.60</td>
            <td>archaludon</td>
            <td>dudunsparce</td>
            <td>10</td>
            <td><a href="reports/cluster_399.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.666666666666666" data-deck-count="3" data-main-pokemon="dudunsparce" data-secondary-pokemon="roaring-moon">
            <td>33</td>
            <td>9.67</td>
            <td>dudunsparce</td>
            <td>roaring-moon</td>
            <td>3</td>
            <td><a href="reports/cluster_33.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.666666666666666" data-deck-count="3" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>59</td>
            <td>9.67</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>3</td>
            <td><a href="reports/cluster_59.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.666666666666666" data-deck-count="3" data-main-pokemon="toedscruel" data-secondary-pokemon="ogerpon">
            <td>89</td>
            <td>9.67</td>
            <td>toedscruel</td>
            <td>ogerpon</td>
            <td>3</td>
            <td><a href="reports/cluster_89.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.666666666666666" data-deck-count="3" data-main-pokemon="metagross" data-secondary-pokemon="munkidori">
            <td>157</td>
            <td>9.67</td>
            <td>metagross</td>
            <td>munkidori</td>
            <td>3</td>
            <td><a href="reports/cluster_157.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.666666666666666" data-deck-count="3" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>249</td>
            <td>9.67</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>3</td>
            <td><a href="reports/cluster_249.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.714285714285714" data-deck-count="7" data-main-pokemon="blaziken" data-secondary-pokemon="munkidori">
            <td>124</td>
            <td>9.71</td>
            <td>blaziken</td>
            <td>munkidori</td>
            <td>7</td>
            <td><a href="reports/cluster_124.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.714285714285714" data-deck-count="7" data-main-pokemon="milotic" data-secondary-pokemon="farigiraf">
            <td>328</td>
            <td>9.71</td>
            <td>milotic</td>
            <td>farigiraf</td>
            <td>7</td>
            <td><a href="reports/cluster_328.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.75" data-deck-count="4" data-main-pokemon="tyranitar" data-secondary-pokemon="budew">
            <td>85</td>
            <td>9.75</td>
            <td>tyranitar</td>
            <td>budew</td>
            <td>4</td>
            <td><a href="reports/cluster_85.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.818181818181818" data-deck-count="11" data-main-pokemon="magneton" data-secondary-pokemon="miraidon">
            <td>425</td>
            <td>9.82</td>
            <td>magneton</td>
            <td>miraidon</td>
            <td>11</td>
            <td><a href="reports/cluster_425.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.875" data-deck-count="16" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>175</td>
            <td>9.88</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>16</td>
            <td><a href="reports/cluster_175.md">Link</a></td>
        </tr>

        <tr data-mean-rank="9.916666666666666" data-deck-count="12" data-main-pokemon="archaludon" data-secondary-pokemon="scizor">
            <td>414</td>
            <td>9.92</td>
            <td>archaludon</td>
            <td>scizor</td>
            <td>12</td>
            <td><a href="reports/cluster_414.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="tinkaton" data-secondary-pokemon="gardevoir">
            <td>50</td>
            <td>10.00</td>
            <td>tinkaton</td>
            <td>gardevoir</td>
            <td>1</td>
            <td><a href="reports/cluster_50.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="gholdengo" data-secondary-pokemon="None">
            <td>60</td>
            <td>10.00</td>
            <td>gholdengo</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_60.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="slaking" data-secondary-pokemon="pidgeot">
            <td>68</td>
            <td>10.00</td>
            <td>slaking</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_68.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="meowscarada" data-secondary-pokemon="pidgeot">
            <td>78</td>
            <td>10.00</td>
            <td>meowscarada</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_78.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="raging-bolt" data-secondary-pokemon="ogerpon">
            <td>100</td>
            <td>10.00</td>
            <td>raging-bolt</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_100.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="dudunsparce" data-secondary-pokemon="exeggutor-alola">
            <td>102</td>
            <td>10.00</td>
            <td>dudunsparce</td>
            <td>exeggutor-alola</td>
            <td>1</td>
            <td><a href="reports/cluster_102.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="armarouge" data-secondary-pokemon="ho-oh">
            <td>110</td>
            <td>10.00</td>
            <td>armarouge</td>
            <td>ho-oh</td>
            <td>1</td>
            <td><a href="reports/cluster_110.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="ursaluna-bloodmoon" data-secondary-pokemon="maractus">
            <td>132</td>
            <td>10.00</td>
            <td>ursaluna-bloodmoon</td>
            <td>maractus</td>
            <td>1</td>
            <td><a href="reports/cluster_132.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="greninja" data-secondary-pokemon="noctowl">
            <td>145</td>
            <td>10.00</td>
            <td>greninja</td>
            <td>noctowl</td>
            <td>1</td>
            <td><a href="reports/cluster_145.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="aegislash" data-secondary-pokemon="iron-thorns">
            <td>162</td>
            <td>10.00</td>
            <td>aegislash</td>
            <td>iron-thorns</td>
            <td>1</td>
            <td><a href="reports/cluster_162.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="ogerpon">
            <td>186</td>
            <td>10.00</td>
            <td>noctowl</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_186.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="seaking" data-secondary-pokemon="thwackey">
            <td>220</td>
            <td>10.00</td>
            <td>seaking</td>
            <td>thwackey</td>
            <td>1</td>
            <td><a href="reports/cluster_220.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="okidogi" data-secondary-pokemon="ogerpon-cornerstone">
            <td>224</td>
            <td>10.00</td>
            <td>okidogi</td>
            <td>ogerpon-cornerstone</td>
            <td>1</td>
            <td><a href="reports/cluster_224.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="toedscruel" data-secondary-pokemon="ogerpon">
            <td>264</td>
            <td>10.00</td>
            <td>toedscruel</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_264.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="greninja" data-secondary-pokemon="xatu">
            <td>324</td>
            <td>10.00</td>
            <td>greninja</td>
            <td>xatu</td>
            <td>1</td>
            <td><a href="reports/cluster_324.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="1" data-main-pokemon="maractus" data-secondary-pokemon="froslass">
            <td>394</td>
            <td>10.00</td>
            <td>maractus</td>
            <td>froslass</td>
            <td>1</td>
            <td><a href="reports/cluster_394.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="2" data-main-pokemon="milotic" data-secondary-pokemon="noivern">
            <td>207</td>
            <td>10.00</td>
            <td>milotic</td>
            <td>noivern</td>
            <td>2</td>
            <td><a href="reports/cluster_207.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="2" data-main-pokemon="froslass" data-secondary-pokemon="munkidori">
            <td>334</td>
            <td>10.00</td>
            <td>froslass</td>
            <td>munkidori</td>
            <td>2</td>
            <td><a href="reports/cluster_334.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="3" data-main-pokemon="gholdengo" data-secondary-pokemon="dudunsparce">
            <td>212</td>
            <td>10.00</td>
            <td>gholdengo</td>
            <td>dudunsparce</td>
            <td>3</td>
            <td><a href="reports/cluster_212.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="3" data-main-pokemon="roaring-moon" data-secondary-pokemon="munkidori">
            <td>321</td>
            <td>10.00</td>
            <td>roaring-moon</td>
            <td>munkidori</td>
            <td>3</td>
            <td><a href="reports/cluster_321.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.0" data-deck-count="4" data-main-pokemon="magcargo" data-secondary-pokemon="ho-oh">
            <td>66</td>
            <td>10.00</td>
            <td>magcargo</td>
            <td>ho-oh</td>
            <td>4</td>
            <td><a href="reports/cluster_66.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.071428571428571" data-deck-count="14" data-main-pokemon="dipplin" data-secondary-pokemon="dipplin">
            <td>408</td>
            <td>10.07</td>
            <td>dipplin</td>
            <td>dipplin</td>
            <td>14</td>
            <td><a href="reports/cluster_408.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.117647058823529" data-deck-count="34" data-main-pokemon="clefairy" data-secondary-pokemon="ogerpon">
            <td>309</td>
            <td>10.12</td>
            <td>clefairy</td>
            <td>ogerpon</td>
            <td>34</td>
            <td><a href="reports/cluster_309.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.153846153846153" data-deck-count="13" data-main-pokemon="grimmsnarl" data-secondary-pokemon="morpeko">
            <td>330</td>
            <td>10.15</td>
            <td>grimmsnarl</td>
            <td>morpeko</td>
            <td>13</td>
            <td><a href="reports/cluster_330.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.2" data-deck-count="10" data-main-pokemon="raging-bolt" data-secondary-pokemon="ogerpon">
            <td>268</td>
            <td>10.20</td>
            <td>raging-bolt</td>
            <td>ogerpon</td>
            <td>10</td>
            <td><a href="reports/cluster_268.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.222222222222221" data-deck-count="9" data-main-pokemon="hydrapple" data-secondary-pokemon="ogerpon">
            <td>69</td>
            <td>10.22</td>
            <td>hydrapple</td>
            <td>ogerpon</td>
            <td>9</td>
            <td><a href="reports/cluster_69.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.222222222222221" data-deck-count="9" data-main-pokemon="armarouge" data-secondary-pokemon="ho-oh">
            <td>79</td>
            <td>10.22</td>
            <td>armarouge</td>
            <td>ho-oh</td>
            <td>9</td>
            <td><a href="reports/cluster_79.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.225" data-deck-count="40" data-main-pokemon="bellibolt" data-secondary-pokemon="kilowattrel">
            <td>270</td>
            <td>10.22</td>
            <td>bellibolt</td>
            <td>kilowattrel</td>
            <td>40</td>
            <td><a href="reports/cluster_270.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.25" data-deck-count="24" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>420</td>
            <td>10.25</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>24</td>
            <td><a href="reports/cluster_420.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.285714285714286" data-deck-count="7" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>380</td>
            <td>10.29</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>7</td>
            <td><a href="reports/cluster_380.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.333333333333334" data-deck-count="3" data-main-pokemon="magmortar" data-secondary-pokemon="budew">
            <td>88</td>
            <td>10.33</td>
            <td>magmortar</td>
            <td>budew</td>
            <td>3</td>
            <td><a href="reports/cluster_88.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.333333333333334" data-deck-count="9" data-main-pokemon="greninja" data-secondary-pokemon="blaziken">
            <td>379</td>
            <td>10.33</td>
            <td>greninja</td>
            <td>blaziken</td>
            <td>9</td>
            <td><a href="reports/cluster_379.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.333333333333334" data-deck-count="24" data-main-pokemon="archaludon" data-secondary-pokemon="scizor">
            <td>80</td>
            <td>10.33</td>
            <td>archaludon</td>
            <td>scizor</td>
            <td>24</td>
            <td><a href="reports/cluster_80.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.375" data-deck-count="8" data-main-pokemon="pecharunt" data-secondary-pokemon="volcanion">
            <td>10</td>
            <td>10.38</td>
            <td>pecharunt</td>
            <td>volcanion</td>
            <td>8</td>
            <td><a href="reports/cluster_10.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.4" data-deck-count="5" data-main-pokemon="ogerpon" data-secondary-pokemon="clefairy">
            <td>383</td>
            <td>10.40</td>
            <td>ogerpon</td>
            <td>clefairy</td>
            <td>5</td>
            <td><a href="reports/cluster_383.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.4" data-deck-count="5" data-main-pokemon="dipplin" data-secondary-pokemon="dipplin">
            <td>424</td>
            <td>10.40</td>
            <td>dipplin</td>
            <td>dipplin</td>
            <td>5</td>
            <td><a href="reports/cluster_424.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.466666666666667" data-deck-count="15" data-main-pokemon="flareon" data-secondary-pokemon="noctowl">
            <td>342</td>
            <td>10.47</td>
            <td>flareon</td>
            <td>noctowl</td>
            <td>15</td>
            <td><a href="reports/cluster_342.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.75" data-deck-count="8" data-main-pokemon="gholdengo" data-secondary-pokemon="dudunsparce">
            <td>135</td>
            <td>10.75</td>
            <td>gholdengo</td>
            <td>dudunsparce</td>
            <td>8</td>
            <td><a href="reports/cluster_135.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.8" data-deck-count="5" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>365</td>
            <td>10.80</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>5</td>
            <td><a href="reports/cluster_365.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.85" data-deck-count="20" data-main-pokemon="roaring-moon" data-secondary-pokemon="flutter-mane">
            <td>305</td>
            <td>10.85</td>
            <td>roaring-moon</td>
            <td>flutter-mane</td>
            <td>20</td>
            <td><a href="reports/cluster_305.md">Link</a></td>
        </tr>

        <tr data-mean-rank="10.9" data-deck-count="10" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>24</td>
            <td>10.90</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>10</td>
            <td><a href="reports/cluster_24.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="glimmora" data-secondary-pokemon="okidogi">
            <td>70</td>
            <td>11.00</td>
            <td>glimmora</td>
            <td>okidogi</td>
            <td>1</td>
            <td><a href="reports/cluster_70.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="ceruledge" data-secondary-pokemon="ting-lu">
            <td>107</td>
            <td>11.00</td>
            <td>ceruledge</td>
            <td>ting-lu</td>
            <td>1</td>
            <td><a href="reports/cluster_107.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="dragapult" data-secondary-pokemon="charizard">
            <td>119</td>
            <td>11.00</td>
            <td>dragapult</td>
            <td>charizard</td>
            <td>1</td>
            <td><a href="reports/cluster_119.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>170</td>
            <td>11.00</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>1</td>
            <td><a href="reports/cluster_170.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="pikachu">
            <td>173</td>
            <td>11.00</td>
            <td>noctowl</td>
            <td>pikachu</td>
            <td>1</td>
            <td><a href="reports/cluster_173.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="miraidon" data-secondary-pokemon="iron-hands">
            <td>179</td>
            <td>11.00</td>
            <td>miraidon</td>
            <td>iron-hands</td>
            <td>1</td>
            <td><a href="reports/cluster_179.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="froslass" data-secondary-pokemon="munkidori">
            <td>181</td>
            <td>11.00</td>
            <td>froslass</td>
            <td>munkidori</td>
            <td>1</td>
            <td><a href="reports/cluster_181.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="archaludon" data-secondary-pokemon="revavroom">
            <td>197</td>
            <td>11.00</td>
            <td>archaludon</td>
            <td>revavroom</td>
            <td>1</td>
            <td><a href="reports/cluster_197.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="clefairy" data-secondary-pokemon="ogerpon">
            <td>248</td>
            <td>11.00</td>
            <td>clefairy</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_248.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="froslass" data-secondary-pokemon="munkidori">
            <td>286</td>
            <td>11.00</td>
            <td>froslass</td>
            <td>munkidori</td>
            <td>1</td>
            <td><a href="reports/cluster_286.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="ceruledge" data-secondary-pokemon="revavroom">
            <td>307</td>
            <td>11.00</td>
            <td>ceruledge</td>
            <td>revavroom</td>
            <td>1</td>
            <td><a href="reports/cluster_307.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="gholdengo" data-secondary-pokemon="scizor">
            <td>367</td>
            <td>11.00</td>
            <td>gholdengo</td>
            <td>scizor</td>
            <td>1</td>
            <td><a href="reports/cluster_367.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="1" data-main-pokemon="zoroark" data-secondary-pokemon="pecharunt">
            <td>393</td>
            <td>11.00</td>
            <td>zoroark</td>
            <td>pecharunt</td>
            <td>1</td>
            <td><a href="reports/cluster_393.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="3" data-main-pokemon="blaziken" data-secondary-pokemon="blaziken">
            <td>51</td>
            <td>11.00</td>
            <td>blaziken</td>
            <td>blaziken</td>
            <td>3</td>
            <td><a href="reports/cluster_51.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="3" data-main-pokemon="dragapult" data-secondary-pokemon="dusknoir">
            <td>376</td>
            <td>11.00</td>
            <td>dragapult</td>
            <td>dusknoir</td>
            <td>3</td>
            <td><a href="reports/cluster_376.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="3" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>427</td>
            <td>11.00</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>3</td>
            <td><a href="reports/cluster_427.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.0" data-deck-count="5" data-main-pokemon="tyranitar" data-secondary-pokemon="dudunsparce">
            <td>83</td>
            <td>11.00</td>
            <td>tyranitar</td>
            <td>dudunsparce</td>
            <td>5</td>
            <td><a href="reports/cluster_83.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.2" data-deck-count="5" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>363</td>
            <td>11.20</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>5</td>
            <td><a href="reports/cluster_363.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.25" data-deck-count="4" data-main-pokemon="iron-crown" data-secondary-pokemon="iron-hands">
            <td>348</td>
            <td>11.25</td>
            <td>iron-crown</td>
            <td>iron-hands</td>
            <td>4</td>
            <td><a href="reports/cluster_348.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.25" data-deck-count="4" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>438</td>
            <td>11.25</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>4</td>
            <td><a href="reports/cluster_438.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.333333333333334" data-deck-count="3" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>64</td>
            <td>11.33</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>3</td>
            <td><a href="reports/cluster_64.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.333333333333334" data-deck-count="3" data-main-pokemon="slaking" data-secondary-pokemon="noctowl">
            <td>82</td>
            <td>11.33</td>
            <td>slaking</td>
            <td>noctowl</td>
            <td>3</td>
            <td><a href="reports/cluster_82.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.333333333333334" data-deck-count="3" data-main-pokemon="azumarill" data-secondary-pokemon="noctowl">
            <td>155</td>
            <td>11.33</td>
            <td>azumarill</td>
            <td>noctowl</td>
            <td>3</td>
            <td><a href="reports/cluster_155.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.4" data-deck-count="5" data-main-pokemon="dragapult" data-secondary-pokemon="budew">
            <td>211</td>
            <td>11.40</td>
            <td>dragapult</td>
            <td>budew</td>
            <td>5</td>
            <td><a href="reports/cluster_211.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.4" data-deck-count="5" data-main-pokemon="sinistcha" data-secondary-pokemon="ogerpon">
            <td>433</td>
            <td>11.40</td>
            <td>sinistcha</td>
            <td>ogerpon</td>
            <td>5</td>
            <td><a href="reports/cluster_433.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.5" data-deck-count="4" data-main-pokemon="feraligatr" data-secondary-pokemon="farigiraf">
            <td>269</td>
            <td>11.50</td>
            <td>feraligatr</td>
            <td>farigiraf</td>
            <td>4</td>
            <td><a href="reports/cluster_269.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.666666666666666" data-deck-count="3" data-main-pokemon="noctowl" data-secondary-pokemon="ogerpon">
            <td>258</td>
            <td>11.67</td>
            <td>noctowl</td>
            <td>ogerpon</td>
            <td>3</td>
            <td><a href="reports/cluster_258.md">Link</a></td>
        </tr>

        <tr data-mean-rank="11.666666666666666" data-deck-count="3" data-main-pokemon="miraidon" data-secondary-pokemon="iron-hands">
            <td>370</td>
            <td>11.67</td>
            <td>miraidon</td>
            <td>iron-hands</td>
            <td>3</td>
            <td><a href="reports/cluster_370.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="cinderace" data-secondary-pokemon="pidgeot">
            <td>44</td>
            <td>12.00</td>
            <td>cinderace</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_44.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="milotic" data-secondary-pokemon="farigiraf">
            <td>45</td>
            <td>12.00</td>
            <td>milotic</td>
            <td>farigiraf</td>
            <td>1</td>
            <td><a href="reports/cluster_45.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="archaludon" data-secondary-pokemon="None">
            <td>108</td>
            <td>12.00</td>
            <td>archaludon</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_108.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="dragapult" data-secondary-pokemon="None">
            <td>111</td>
            <td>12.00</td>
            <td>dragapult</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_111.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="iron-hands" data-secondary-pokemon="iron-crown">
            <td>142</td>
            <td>12.00</td>
            <td>iron-hands</td>
            <td>iron-crown</td>
            <td>1</td>
            <td><a href="reports/cluster_142.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="palafin" data-secondary-pokemon="pecharunt">
            <td>191</td>
            <td>12.00</td>
            <td>palafin</td>
            <td>pecharunt</td>
            <td>1</td>
            <td><a href="reports/cluster_191.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>215</td>
            <td>12.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_215.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="forretress" data-secondary-pokemon="noctowl">
            <td>233</td>
            <td>12.00</td>
            <td>forretress</td>
            <td>noctowl</td>
            <td>1</td>
            <td><a href="reports/cluster_233.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="metang" data-secondary-pokemon="archaludon">
            <td>255</td>
            <td>12.00</td>
            <td>metang</td>
            <td>archaludon</td>
            <td>1</td>
            <td><a href="reports/cluster_255.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="conkeldurr" data-secondary-pokemon="pidgeot">
            <td>297</td>
            <td>12.00</td>
            <td>conkeldurr</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_297.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="1" data-main-pokemon="archaludon" data-secondary-pokemon="squawkabilly">
            <td>418</td>
            <td>12.00</td>
            <td>archaludon</td>
            <td>squawkabilly</td>
            <td>1</td>
            <td><a href="reports/cluster_418.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="2" data-main-pokemon="ceruledge" data-secondary-pokemon="squawkabilly">
            <td>188</td>
            <td>12.00</td>
            <td>ceruledge</td>
            <td>squawkabilly</td>
            <td>2</td>
            <td><a href="reports/cluster_188.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="3" data-main-pokemon="ogerpon" data-secondary-pokemon="walking-wake">
            <td>214</td>
            <td>12.00</td>
            <td>ogerpon</td>
            <td>walking-wake</td>
            <td>3</td>
            <td><a href="reports/cluster_214.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="3" data-main-pokemon="conkeldurr" data-secondary-pokemon="brute-bonnet">
            <td>274</td>
            <td>12.00</td>
            <td>conkeldurr</td>
            <td>brute-bonnet</td>
            <td>3</td>
            <td><a href="reports/cluster_274.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="3" data-main-pokemon="conkeldurr" data-secondary-pokemon="dudunsparce">
            <td>405</td>
            <td>12.00</td>
            <td>conkeldurr</td>
            <td>dudunsparce</td>
            <td>3</td>
            <td><a href="reports/cluster_405.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.0" data-deck-count="7" data-main-pokemon="baxcalibur" data-secondary-pokemon="revavroom">
            <td>43</td>
            <td>12.00</td>
            <td>baxcalibur</td>
            <td>revavroom</td>
            <td>7</td>
            <td><a href="reports/cluster_43.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.375" data-deck-count="8" data-main-pokemon="flareon" data-secondary-pokemon="noctowl">
            <td>266</td>
            <td>12.38</td>
            <td>flareon</td>
            <td>noctowl</td>
            <td>8</td>
            <td><a href="reports/cluster_266.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.375" data-deck-count="8" data-main-pokemon="noctowl" data-secondary-pokemon="darmanitan">
            <td>373</td>
            <td>12.38</td>
            <td>noctowl</td>
            <td>darmanitan</td>
            <td>8</td>
            <td><a href="reports/cluster_373.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.5" data-deck-count="2" data-main-pokemon="wailord" data-secondary-pokemon="baxcalibur">
            <td>28</td>
            <td>12.50</td>
            <td>wailord</td>
            <td>baxcalibur</td>
            <td>2</td>
            <td><a href="reports/cluster_28.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.5" data-deck-count="2" data-main-pokemon="miraidon" data-secondary-pokemon="iron-hands">
            <td>237</td>
            <td>12.50</td>
            <td>miraidon</td>
            <td>iron-hands</td>
            <td>2</td>
            <td><a href="reports/cluster_237.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.5" data-deck-count="2" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>318</td>
            <td>12.50</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>2</td>
            <td><a href="reports/cluster_318.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.5" data-deck-count="2" data-main-pokemon="gholdengo" data-secondary-pokemon="None">
            <td>366</td>
            <td>12.50</td>
            <td>gholdengo</td>
            <td>None</td>
            <td>2</td>
            <td><a href="reports/cluster_366.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.5" data-deck-count="2" data-main-pokemon="clefairy" data-secondary-pokemon="ogerpon">
            <td>406</td>
            <td>12.50</td>
            <td>clefairy</td>
            <td>ogerpon</td>
            <td>2</td>
            <td><a href="reports/cluster_406.md">Link</a></td>
        </tr>

        <tr data-mean-rank="12.9" data-deck-count="10" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>319</td>
            <td>12.90</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>10</td>
            <td><a href="reports/cluster_319.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="1" data-main-pokemon="tyranitar" data-secondary-pokemon="dudunsparce">
            <td>26</td>
            <td>13.00</td>
            <td>tyranitar</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_26.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="1" data-main-pokemon="incineroar" data-secondary-pokemon="pidgeot">
            <td>35</td>
            <td>13.00</td>
            <td>incineroar</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_35.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="1" data-main-pokemon="miraidon" data-secondary-pokemon="iron-hands">
            <td>36</td>
            <td>13.00</td>
            <td>miraidon</td>
            <td>iron-hands</td>
            <td>1</td>
            <td><a href="reports/cluster_36.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="1" data-main-pokemon="ceruledge" data-secondary-pokemon="None">
            <td>192</td>
            <td>13.00</td>
            <td>ceruledge</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_192.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="1" data-main-pokemon="hydreigon" data-secondary-pokemon="pidgeot">
            <td>242</td>
            <td>13.00</td>
            <td>hydreigon</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_242.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="1" data-main-pokemon="palafin" data-secondary-pokemon="weavile">
            <td>288</td>
            <td>13.00</td>
            <td>palafin</td>
            <td>weavile</td>
            <td>1</td>
            <td><a href="reports/cluster_288.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="1" data-main-pokemon="miraidon" data-secondary-pokemon="iron-hands">
            <td>296</td>
            <td>13.00</td>
            <td>miraidon</td>
            <td>iron-hands</td>
            <td>1</td>
            <td><a href="reports/cluster_296.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="2" data-main-pokemon="typhlosion" data-secondary-pokemon="zacian-crowned">
            <td>388</td>
            <td>13.00</td>
            <td>typhlosion</td>
            <td>zacian-crowned</td>
            <td>2</td>
            <td><a href="reports/cluster_388.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.0" data-deck-count="2" data-main-pokemon="baxcalibur" data-secondary-pokemon="chien-pao">
            <td>447</td>
            <td>13.00</td>
            <td>baxcalibur</td>
            <td>chien-pao</td>
            <td>2</td>
            <td><a href="reports/cluster_447.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.166666666666666" data-deck-count="6" data-main-pokemon="gholdengo" data-secondary-pokemon="togekiss">
            <td>81</td>
            <td>13.17</td>
            <td>gholdengo</td>
            <td>togekiss</td>
            <td>6</td>
            <td><a href="reports/cluster_81.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.2" data-deck-count="5" data-main-pokemon="feraligatr" data-secondary-pokemon="munkidori">
            <td>349</td>
            <td>13.20</td>
            <td>feraligatr</td>
            <td>munkidori</td>
            <td>5</td>
            <td><a href="reports/cluster_349.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.25" data-deck-count="4" data-main-pokemon="ceruledge" data-secondary-pokemon="flareon">
            <td>440</td>
            <td>13.25</td>
            <td>ceruledge</td>
            <td>flareon</td>
            <td>4</td>
            <td><a href="reports/cluster_440.md">Link</a></td>
        </tr>

        <tr data-mean-rank="13.25" data-deck-count="12" data-main-pokemon="gholdengo" data-secondary-pokemon="togekiss">
            <td>240</td>
            <td>13.25</td>
            <td>gholdengo</td>
            <td>togekiss</td>
            <td>12</td>
            <td><a href="reports/cluster_240.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="dudunsparce" data-secondary-pokemon="yanmega">
            <td>7</td>
            <td>14.00</td>
            <td>dudunsparce</td>
            <td>yanmega</td>
            <td>1</td>
            <td><a href="reports/cluster_7.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="drednaw" data-secondary-pokemon="crustle">
            <td>90</td>
            <td>14.00</td>
            <td>drednaw</td>
            <td>crustle</td>
            <td>1</td>
            <td><a href="reports/cluster_90.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>189</td>
            <td>14.00</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_189.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>196</td>
            <td>14.00</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>1</td>
            <td><a href="reports/cluster_196.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="rillaboom" data-secondary-pokemon="seaking">
            <td>199</td>
            <td>14.00</td>
            <td>rillaboom</td>
            <td>seaking</td>
            <td>1</td>
            <td><a href="reports/cluster_199.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="palafin" data-secondary-pokemon="munkidori">
            <td>204</td>
            <td>14.00</td>
            <td>palafin</td>
            <td>munkidori</td>
            <td>1</td>
            <td><a href="reports/cluster_204.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="gholdengo" data-secondary-pokemon="dudunsparce">
            <td>230</td>
            <td>14.00</td>
            <td>gholdengo</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_230.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="dudunsparce">
            <td>246</td>
            <td>14.00</td>
            <td>charizard</td>
            <td>dudunsparce</td>
            <td>1</td>
            <td><a href="reports/cluster_246.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="terapagos">
            <td>247</td>
            <td>14.00</td>
            <td>noctowl</td>
            <td>terapagos</td>
            <td>1</td>
            <td><a href="reports/cluster_247.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="zoroark" data-secondary-pokemon="darmanitan">
            <td>252</td>
            <td>14.00</td>
            <td>zoroark</td>
            <td>darmanitan</td>
            <td>1</td>
            <td><a href="reports/cluster_252.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="xatu" data-secondary-pokemon="clefairy">
            <td>256</td>
            <td>14.00</td>
            <td>xatu</td>
            <td>clefairy</td>
            <td>1</td>
            <td><a href="reports/cluster_256.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="1" data-main-pokemon="terapagos" data-secondary-pokemon="pikachu">
            <td>272</td>
            <td>14.00</td>
            <td>terapagos</td>
            <td>pikachu</td>
            <td>1</td>
            <td><a href="reports/cluster_272.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.0" data-deck-count="2" data-main-pokemon="dragapult" data-secondary-pokemon="pidgeot">
            <td>333</td>
            <td>14.00</td>
            <td>dragapult</td>
            <td>pidgeot</td>
            <td>2</td>
            <td><a href="reports/cluster_333.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.333333333333334" data-deck-count="3" data-main-pokemon="metagross" data-secondary-pokemon="revavroom">
            <td>401</td>
            <td>14.33</td>
            <td>metagross</td>
            <td>revavroom</td>
            <td>3</td>
            <td><a href="reports/cluster_401.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.5" data-deck-count="2" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>149</td>
            <td>14.50</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>2</td>
            <td><a href="reports/cluster_149.md">Link</a></td>
        </tr>

        <tr data-mean-rank="14.5" data-deck-count="2" data-main-pokemon="toedscruel" data-secondary-pokemon="ogerpon">
            <td>218</td>
            <td>14.50</td>
            <td>toedscruel</td>
            <td>ogerpon</td>
            <td>2</td>
            <td><a href="reports/cluster_218.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="espathra" data-secondary-pokemon="froslass">
            <td>115</td>
            <td>15.00</td>
            <td>espathra</td>
            <td>froslass</td>
            <td>1</td>
            <td><a href="reports/cluster_115.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="farigiraf" data-secondary-pokemon="espathra">
            <td>116</td>
            <td>15.00</td>
            <td>farigiraf</td>
            <td>espathra</td>
            <td>1</td>
            <td><a href="reports/cluster_116.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="yanmega" data-secondary-pokemon="crustle">
            <td>118</td>
            <td>15.00</td>
            <td>yanmega</td>
            <td>crustle</td>
            <td>1</td>
            <td><a href="reports/cluster_118.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>158</td>
            <td>15.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_158.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="froslass" data-secondary-pokemon="lycanroc">
            <td>165</td>
            <td>15.00</td>
            <td>froslass</td>
            <td>lycanroc</td>
            <td>1</td>
            <td><a href="reports/cluster_165.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="okidogi" data-secondary-pokemon="None">
            <td>172</td>
            <td>15.00</td>
            <td>okidogi</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_172.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="aegislash" data-secondary-pokemon="rabsca">
            <td>203</td>
            <td>15.00</td>
            <td>aegislash</td>
            <td>rabsca</td>
            <td>1</td>
            <td><a href="reports/cluster_203.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="zoroark" data-secondary-pokemon="reshiram">
            <td>228</td>
            <td>15.00</td>
            <td>zoroark</td>
            <td>reshiram</td>
            <td>1</td>
            <td><a href="reports/cluster_228.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="squawkabilly" data-secondary-pokemon="klawf">
            <td>232</td>
            <td>15.00</td>
            <td>squawkabilly</td>
            <td>klawf</td>
            <td>1</td>
            <td><a href="reports/cluster_232.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="ogerpon-cornerstone" data-secondary-pokemon="mimikyu">
            <td>290</td>
            <td>15.00</td>
            <td>ogerpon-cornerstone</td>
            <td>mimikyu</td>
            <td>1</td>
            <td><a href="reports/cluster_290.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="gardevoir" data-secondary-pokemon="munkidori">
            <td>337</td>
            <td>15.00</td>
            <td>gardevoir</td>
            <td>munkidori</td>
            <td>1</td>
            <td><a href="reports/cluster_337.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>413</td>
            <td>15.00</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_413.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="2" data-main-pokemon="gholdengo" data-secondary-pokemon="budew">
            <td>229</td>
            <td>15.00</td>
            <td>gholdengo</td>
            <td>budew</td>
            <td>2</td>
            <td><a href="reports/cluster_229.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.0" data-deck-count="2" data-main-pokemon="iron-crown" data-secondary-pokemon="iron-crown">
            <td>308</td>
            <td>15.00</td>
            <td>iron-crown</td>
            <td>iron-crown</td>
            <td>2</td>
            <td><a href="reports/cluster_308.md">Link</a></td>
        </tr>

        <tr data-mean-rank="15.5" data-deck-count="2" data-main-pokemon="archaludon" data-secondary-pokemon="dubwool">
            <td>322</td>
            <td>15.50</td>
            <td>archaludon</td>
            <td>dubwool</td>
            <td>2</td>
            <td><a href="reports/cluster_322.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="milotic" data-secondary-pokemon="noivern">
            <td>14</td>
            <td>16.00</td>
            <td>milotic</td>
            <td>noivern</td>
            <td>1</td>
            <td><a href="reports/cluster_14.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="ogerpon" data-secondary-pokemon="raging-bolt">
            <td>30</td>
            <td>16.00</td>
            <td>ogerpon</td>
            <td>raging-bolt</td>
            <td>1</td>
            <td><a href="reports/cluster_30.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="regidrago" data-secondary-pokemon="dragapult">
            <td>42</td>
            <td>16.00</td>
            <td>regidrago</td>
            <td>dragapult</td>
            <td>1</td>
            <td><a href="reports/cluster_42.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="lycanroc" data-secondary-pokemon="dodrio">
            <td>63</td>
            <td>16.00</td>
            <td>lycanroc</td>
            <td>dodrio</td>
            <td>1</td>
            <td><a href="reports/cluster_63.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="ogerpon" data-secondary-pokemon="sinistcha">
            <td>77</td>
            <td>16.00</td>
            <td>ogerpon</td>
            <td>sinistcha</td>
            <td>1</td>
            <td><a href="reports/cluster_77.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="iron-thorns" data-secondary-pokemon="None">
            <td>161</td>
            <td>16.00</td>
            <td>iron-thorns</td>
            <td>None</td>
            <td>1</td>
            <td><a href="reports/cluster_161.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>163</td>
            <td>16.00</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>1</td>
            <td><a href="reports/cluster_163.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="hydreigon" data-secondary-pokemon="bronzong">
            <td>184</td>
            <td>16.00</td>
            <td>hydreigon</td>
            <td>bronzong</td>
            <td>1</td>
            <td><a href="reports/cluster_184.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="charizard" data-secondary-pokemon="pidgeot">
            <td>213</td>
            <td>16.00</td>
            <td>charizard</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_213.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="pidgeot" data-secondary-pokemon="milotic">
            <td>267</td>
            <td>16.00</td>
            <td>pidgeot</td>
            <td>milotic</td>
            <td>1</td>
            <td><a href="reports/cluster_267.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="ho-oh" data-secondary-pokemon="armarouge">
            <td>298</td>
            <td>16.00</td>
            <td>ho-oh</td>
            <td>armarouge</td>
            <td>1</td>
            <td><a href="reports/cluster_298.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="typhlosion" data-secondary-pokemon="incineroar">
            <td>317</td>
            <td>16.00</td>
            <td>typhlosion</td>
            <td>incineroar</td>
            <td>1</td>
            <td><a href="reports/cluster_317.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="hydreigon" data-secondary-pokemon="lapras">
            <td>343</td>
            <td>16.00</td>
            <td>hydreigon</td>
            <td>lapras</td>
            <td>1</td>
            <td><a href="reports/cluster_343.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="mamoswine" data-secondary-pokemon="pidgeot">
            <td>346</td>
            <td>16.00</td>
            <td>mamoswine</td>
            <td>pidgeot</td>
            <td>1</td>
            <td><a href="reports/cluster_346.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="magnezone" data-secondary-pokemon="miraidon">
            <td>357</td>
            <td>16.00</td>
            <td>magnezone</td>
            <td>miraidon</td>
            <td>1</td>
            <td><a href="reports/cluster_357.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="slowking" data-secondary-pokemon="xatu">
            <td>374</td>
            <td>16.00</td>
            <td>slowking</td>
            <td>xatu</td>
            <td>1</td>
            <td><a href="reports/cluster_374.md">Link</a></td>
        </tr>

        <tr data-mean-rank="16.0" data-deck-count="1" data-main-pokemon="noctowl" data-secondary-pokemon="ogerpon">
            <td>391</td>
            <td>16.00</td>
            <td>noctowl</td>
            <td>ogerpon</td>
            <td>1</td>
            <td><a href="reports/cluster_391.md">Link</a></td>
        </tr>

    </tbody>
</table>
