/* Slice and Dice: Verificar as entradas mensais no hospital que aconteceram na cidade de São Paulo no ano de 2021 */
SELECT "Data - FkData"."Mes" AS "Data - FkData__Mes", sum("public"."saude_fatos"."Registro_ocorrencia") AS "sum"
FROM "public"."saude_fatos"
LEFT JOIN "public"."data" "Data - FkData" ON "public"."saude_fatos"."fkData" = "Data - FkData"."pkData" LEFT JOIN "public"."saude_local" "Saude Local - FkLocal" ON "public"."saude_fatos"."fkLocal" = "Saude Local - FkLocal"."pkLocal"
WHERE ("Data - FkData"."DataCompleta" >= timestamp with time zone '2021-01-01 00:00:00.000-03:00'
   AND "Data - FkData"."DataCompleta" < timestamp with time zone '2022-01-01 00:00:00.000-03:00' AND "Saude Local - FkLocal"."Municipio" = 'SAO PAULO')
GROUP BY "Data - FkData"."Mes"
ORDER BY 
    CASE 
        WHEN "Data - FkData"."Mes" = '1' THEN 1
        WHEN "Data - FkData"."Mes" = '2' THEN 2
        WHEN "Data - FkData"."Mes" = '3' THEN 3
        WHEN "Data - FkData"."Mes" = '4' THEN 4
        WHEN "Data - FkData"."Mes" = '5' THEN 5
        WHEN "Data - FkData"."Mes" = '6' THEN 6
        WHEN "Data - FkData"."Mes" = '7' THEN 7
        WHEN "Data - FkData"."Mes" = '8' THEN 8
        WHEN "Data - FkData"."Mes" = '9' THEN 9
        WHEN "Data - FkData"."Mes" = '10' THEN 10
        WHEN "Data - FkData"."Mes" = '11' THEN 11
        WHEN "Data - FkData"."Mes" = '12' THEN 12
    END
ASC

/* Drill Down: Verificar por semanal quantas gestantes entraram no hospital */
SELECT (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) AS "Data - FkData__DataCompleta", sum("public"."saude_fatos"."Gestante") AS "sum"
FROM "public"."saude_fatos"
LEFT JOIN "public"."data" "Data - FkData" ON "public"."saude_fatos"."fkData" = "Data - FkData"."pkData"
WHERE ("Data - FkData"."Ano" = '2021'
    OR "Data - FkData"."Ano" = '2022')
GROUP BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day'))
ORDER BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) ASC

/* Roll Up: verificar precipitacao total por mes por regiao no nos primeiros 4 meses de 2021 */
SELECT date_trunc('month', "Data - FkData"."DataCompleta") AS "Data - FkData__DataCompleta", "Clima Local - FkEstacao"."region" AS "Clima Local - FkEstacao__region", sum("public"."clima_fatos"."PrecipitacaoTotal") AS "sum"
FROM "public"."clima_fatos"
LEFT JOIN "public"."clima_local" "Clima Local - FkEstacao" ON "public"."clima_fatos"."fkEstacao" = "Clima Local - FkEstacao"."pkEstacao" LEFT JOIN "public"."data" "Data - FkData" ON "public"."clima_fatos"."fkData" = "Data - FkData"."pkData"
WHERE ("Data - FkData"."DataCompleta" >= timestamp with time zone '2021-01-01 00:00:00.000-03:00'
   AND "Data - FkData"."DataCompleta" < timestamp with time zone '2021-05-01 00:00:00.000-03:00')
GROUP BY date_trunc('month', "Data - FkData"."DataCompleta"), "Clima Local - FkEstacao"."region"
ORDER BY date_trunc('month', "Data - FkData"."DataCompleta") ASC, "Clima Local - FkEstacao"."region" ASC

/* pivot: */
SELECT (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) AS "Data - FkData__DataCompleta", "Saude Local - FkLocal"."Estado" AS "Saude Local - FkLocal__Estado", sum("public"."saude_fatos"."Registro_ocorrencia") AS "sum"
FROM "public"."saude_fatos"
LEFT JOIN "public"."data" "Data - FkData" ON "public"."saude_fatos"."fkData" = "Data - FkData"."pkData" LEFT JOIN "public"."saude_local" "Saude Local - FkLocal" ON "public"."saude_fatos"."fkLocal" = "Saude Local - FkLocal"."pkLocal"
WHERE (("Data - FkData"."Semana" = '1'
    OR "Data - FkData"."Semana" = '2' OR "Data - FkData"."Semana" = '3' OR "Data - FkData"."Semana" = '4' OR "Data - FkData"."Semana" = '5')
   AND "Data - FkData"."Ano" = '2021')
GROUP BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')), "Saude Local - FkLocal"."Estado"
ORDER BY (CAST(date_trunc('week', ("Data - FkData"."DataCompleta" + (INTERVAL '1 day'))) AS timestamp) + (INTERVAL '-1 day')) ASC, "Saude Local - FkLocal"."Estado" ASC

/* drill across: pegar a soma diaria de pessoas com algum virus e a soma da preciptacao durante os primeiros 4 meses de 2021 */
SELECT dataRO as "data", RO as "Registro Ocorrencia", Prec as "Precipitacao"
FROM ( SELECT "Data - FkData"."DataCompleta", sum("public"."saude_fatos"."Registro_ocorrencia")
        FROM "public"."saude_fatos"
        LEFT JOIN "public"."data" "Data - FkData" ON "public"."saude_fatos"."fkData" = "Data - FkData"."pkData"
        WHERE (("Data - FkData"."Mes-Ano" = '2021-1'
            OR "Data - FkData"."Mes-Ano" = '2021-2' OR "Data - FkData"."Mes-Ano" = '2021-3' OR "Data - FkData"."Mes-Ano" = '2021-4')
        AND ("public"."saude_fatos"."fkGrupoDoenca" <> 0 OR "public"."saude_fatos"."fkGrupoDoenca" IS NULL))
        GROUP BY "Data - FkData"."DataCompleta"
      ) AS a(dataRO, RO)
    JOIN
    (SELECT "Data - FkData"."DataCompleta", sum("public"."clima_fatos"."PrecipitacaoTotal")
        FROM "public"."clima_fatos"
        LEFT JOIN "public"."data" "Data - FkData" ON "public"."clima_fatos"."fkData" = "Data - FkData"."pkData"
        WHERE ("Data - FkData"."Mes-Ano" = '2021-1'
            OR "Data - FkData"."Mes-Ano" = '2021-2' OR "Data - FkData"."Mes-Ano" = '2021-3' OR "Data - FkData"."Mes-Ano" = '2021-4')
        GROUP BY "Data - FkData"."DataCompleta"
    ) AS b(dataPrec, Prec)
    ON dataRO = dataPrec
    ORDER BY dataRO ASC