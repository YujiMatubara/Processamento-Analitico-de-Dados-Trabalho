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